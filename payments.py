import os
import stripe

from datetime import datetime
from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session
from dotenv import load_dotenv

from .database import get_db
from .models import User, Subscription, Payment


# =========================================================
# ENVIRONMENT
# =========================================================

load_dotenv()

STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET")
STRIPE_PRO_PRICE_ID = os.getenv("STRIPE_PRO_PRICE_ID")

if not STRIPE_SECRET_KEY:
    raise RuntimeError("STRIPE_SECRET_KEY is not configured.")

stripe.api_key = STRIPE_SECRET_KEY


# =========================================================
# ROUTER
# =========================================================

router = APIRouter(
    prefix="/payments",
    tags=["Payments"]
)


# =========================================================
# STRIPE CHECKOUT
# =========================================================

@router.post("/checkout")
async def create_checkout_session(
    request: Request,
    db: Session = Depends(get_db)
):
    """
    Creates a Stripe Checkout Session
    for the Toolora Pro subscription.
    """

    user_id = getattr(request.state, "user_id", None)

    if not user_id:
        raise HTTPException(
            status_code=401,
            detail="You must be logged in."
        )

    user = (
        db.query(User)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found."
        )

    # Check existing subscription
    subscription = (
        db.query(Subscription)
        .filter(
            Subscription.user_id == user.id
        )
        .first()
    )

    # Prevent duplicate active subscriptions
    if (
        subscription
        and subscription.plan == "pro"
        and subscription.status == "active"
    ):
        raise HTTPException(
            status_code=400,
            detail="You already have an active Pro subscription."
        )

    try:

        # Create Stripe customer if necessary
        if (
            subscription
            and subscription.stripe_customer_id
        ):
            customer_id = (
                subscription.stripe_customer_id
            )

        else:

            customer = stripe.Customer.create(
                email=user.email,
                metadata={
                    "toolora_user_id": str(user.id)
                }
            )

            customer_id = customer.id

        # Create Checkout Session
        checkout_session = stripe.checkout.Session.create(

            mode="subscription",

            customer=customer_id,

            line_items=[
                {
                    "price": STRIPE_PRO_PRICE_ID,
                    "quantity": 1
                }
            ],

            success_url=(
                str(request.base_url)
                + "payments/success"
                + "?session_id={CHECKOUT_SESSION_ID}"
            ),

            cancel_url=(
                str(request.base_url)
                + "pricing"
            ),

            metadata={
                "toolora_user_id": str(user.id)
            },

            subscription_data={
                "metadata": {
                    "toolora_user_id": str(user.id)
                }
            }
        )

        return {
            "success": True,
            "checkout_url": checkout_session.url
        }

    except stripe.error.StripeError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


# =========================================================
# PAYMENT SUCCESS
# =========================================================

@router.get("/success")
async def payment_success():

    return {
        "success": True,
        "message": (
            "Payment completed. "
            "Your Pro subscription is being activated."
        )
    }


# =========================================================
# STRIPE WEBHOOK
# =========================================================

@router.post("/webhook")
async def stripe_webhook(
    request: Request,
    db: Session = Depends(get_db)
):
    """
    Stripe sends payment/subscription events here.

    Pro activation is performed through verified
    Stripe webhook events, not simply by visiting
    the success page.
    """

    payload = await request.body()

    signature = request.headers.get(
        "stripe-signature"
    )

    if not signature:
        raise HTTPException(
            status_code=400,
            detail="Missing Stripe signature."
        )

    try:

        event = stripe.Webhook.construct_event(
            payload,
            signature,
            STRIPE_WEBHOOK_SECRET
        )

    except ValueError:

        raise HTTPException(
            status_code=400,
            detail="Invalid webhook payload."
        )

    except stripe.error.SignatureVerificationError:

        raise HTTPException(
            status_code=400,
            detail="Invalid webhook signature."
        )

    event_type = event["type"]
    event_object = event["data"]["object"]

    # =====================================================
    # CHECKOUT COMPLETED
    # =====================================================

    if event_type == "checkout.session.completed":

        session = event_object

        user_id = (
            session
            .get("metadata", {})
            .get("toolora_user_id")
        )

        customer_id = session.get(
            "customer"
        )

        stripe_subscription_id = session.get(
            "subscription"
        )

        if not user_id:
            return {"received": True}

        user = (
            db.query(User)
            .filter(
                User.id == int(user_id)
            )
            .first()
        )

        if not user:
            return {"received": True}

        subscription = (
            db.query(Subscription)
            .filter(
                Subscription.user_id == user.id
            )
            .first()
        )

        if not subscription:

            subscription = Subscription(
                user_id=user.id,
                plan="free",
                status="inactive"
            )

            db.add(subscription)

        subscription.stripe_customer_id = (
            customer_id
        )

        subscription.stripe_subscription_id = (
            stripe_subscription_id
        )

        db.commit()

    # =====================================================
    # SUBSCRIPTION CREATED / UPDATED
    # =====================================================

    elif event_type in [
        "customer.subscription.created",
        "customer.subscription.updated"
    ]:

        stripe_subscription = event_object

        subscription_id = (
            stripe_subscription["id"]
        )

        metadata = (
            stripe_subscription
            .get("metadata", {})
        )

        user_id = metadata.get(
            "toolora_user_id"
        )

        subscription = (
            db.query(Subscription)
            .filter(
                Subscription.stripe_subscription_id
                == subscription_id
            )
            .first()
        )

        # Find user if subscription isn't stored yet
        if not subscription and user_id:

            subscription = (
                db.query(Subscription)
                .filter(
                    Subscription.user_id
                    == int(user_id)
                )
                .first()
            )

        if subscription:

            subscription.stripe_subscription_id = (
                subscription_id
            )

            subscription.stripe_customer_id = (
                stripe_subscription.get(
                    "customer"
                )
            )

            stripe_status = (
                stripe_subscription.get(
                    "status"
                )
            )

            subscription.status = (
                stripe_status
            )

            # Activate Pro only when Stripe says active
            if stripe_status == "active":

                subscription.plan = "pro"

            else:

                subscription.plan = "free"

            # Stripe timestamps
            period_start = (
                stripe_subscription.get(
                    "current_period_start"
                )
            )

            period_end = (
                stripe_subscription.get(
                    "current_period_end"
                )
            )

            if period_start:

                subscription.current_period_start = (
                    datetime.fromtimestamp(
                        period_start
                    )
                )

            if period_end:

                subscription.current_period_end = (
                    datetime.fromtimestamp(
                        period_end
                    )
                )

            db.commit()

    # =====================================================
    # SUBSCRIPTION CANCELED
    # =====================================================

    elif event_type == "customer.subscription.deleted":

        stripe_subscription = event_object

        subscription_id = (
            stripe_subscription["id"]
        )

        subscription = (
            db.query(Subscription)
            .filter(
                Subscription.stripe_subscription_id
                == subscription_id
            )
            .first()
        )

        if subscription:

            subscription.status = "canceled"

            subscription.plan = "free"

            db.commit()

    # =====================================================
    # INVOICE PAYMENT SUCCEEDED
    # =====================================================

    elif event_type == "invoice.payment_succeeded":

        invoice = event_object

        customer_id = invoice.get(
            "customer"
        )

        subscription_id = invoice.get(
            "subscription"
        )

        amount = invoice.get(
            "amount_paid",
            0
        )

        currency = invoice.get(
            "currency",
            "usd"
        )

        # Find Toolora subscription
        subscription = (
            db.query(Subscription)
            .filter(
                Subscription.stripe_customer_id
                == customer_id
            )
            .first()
        )

        if subscription:

            # Prevent duplicate payment records
            existing_payment = (
                db.query(Payment)
                .filter(
                    Payment.stripe_payment_id
                    == invoice.get("id")
                )
                .first()
            )

            if not existing_payment:

                payment = Payment(

                    user_id=subscription.user_id,

                    stripe_payment_id=invoice.get(
                        "id"
                    ),

                    stripe_customer_id=customer_id,

                    stripe_subscription_id=(
                        subscription_id
                    ),

                    amount=amount,

                    currency=currency,

                    status="succeeded"
                )

                db.add(payment)

                db.commit()

    # =====================================================
    # INVOICE PAYMENT FAILED
    # =====================================================

    elif event_type == "invoice.payment_failed":

        invoice = event_object

        customer_id = invoice.get(
            "customer"
        )

        subscription = (
            db.query(Subscription)
            .filter(
                Subscription.stripe_customer_id
                == customer_id
            )
            .first()
        )

        if subscription:

            subscription.status = (
                "payment_failed"
            )

            subscription.plan = "free"

            db.commit()

    return {
        "received": True
    }


# =========================================================
# CANCEL SUBSCRIPTION
# =========================================================

@router.post("/cancel")
async def cancel_subscription(
    request: Request,
    db: Session = Depends(get_db)
):

    user_id = getattr(
        request.state,
        "user_id",
        None
    )

    if not user_id:

        raise HTTPException(
            status_code=401,
            detail="You must be logged in."
        )

    subscription = (
        db.query(Subscription)
        .filter(
            Subscription.user_id == user_id
        )
        .first()
    )

    if not subscription:

        raise HTTPException(
            status_code=404,
            detail="Subscription not found."
        )

    if not subscription.stripe_subscription_id:

        raise HTTPException(
            status_code=400,
            detail="Stripe subscription not found."
        )

    try:

        stripe.Subscription.cancel(
            subscription.stripe_subscription_id
        )

        subscription.status = "canceled"
        subscription.plan = "free"

        db.commit()

        return {
            "success": True,
            "message": "Subscription canceled."
        }

    except stripe.error.StripeError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )


# =========================================================
# CURRENT SUBSCRIPTION
# =========================================================

@router.get("/subscription")
async def get_subscription(
    request: Request,
    db: Session = Depends(get_db)
):

    user_id = getattr(
        request.state,
        "user_id",
        None
    )

    if not user_id:

        raise HTTPException(
            status_code=401,
            detail="You must be logged in."
        )

    subscription = (
        db.query(Subscription)
        .filter(
            Subscription.user_id == user_id
        )
        .first()
    )

    if not subscription:

        return {
            "plan": "free",
            "status": "inactive"
        }

    return {
        "plan": subscription.plan,
        "status": subscription.status,
        "current_period_start": (
            subscription.current_period_start
        ),
        "current_period_end": (
            subscription.current_period_end
        )
    }


# =========================================================
# CHECK PRO ACCESS
# =========================================================

def user_has_pro(
    user_id: int,
    db: Session
) -> bool:

    subscription = (
        db.query(Subscription)
        .filter(
            Subscription.user_id == user_id,
            Subscription.plan == "pro",
            Subscription.status == "active"
        )
        .first()
    )

    return subscription is not None
