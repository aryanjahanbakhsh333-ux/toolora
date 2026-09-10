import os
import logging
from datetime import datetime
from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(
    prefix="/admin/notifications",
    tags=["Admin Notifications"]
)

logger = logging.getLogger("toolora_admin")


# =========================================================
# ADMIN NOTIFICATION SETTINGS
# =========================================================

ADMIN_NOTIFICATION_ENABLED = (
    os.getenv(
        "ADMIN_NOTIFICATION_ENABLED",
        "true"
    ).lower() == "true"
)


# =========================================================
# NOTIFICATION FUNCTION
# =========================================================

def send_admin_notification(
    event_type: str,
    message: str
):
    """
    Creates a safe administrative notification.

    Do NOT put private user content inside
    the notification message.
    """

    if not ADMIN_NOTIFICATION_ENABLED:
        return False

    notification = {
        "event": event_type,
        "message": message,
        "timestamp": datetime.utcnow().isoformat()
    }

    # Temporary server log
    logger.info(
        "TOOLORA ADMIN NOTIFICATION: %s",
        notification
    )

    # This function can later be connected
    # to a real push-notification service.

    return True


# =========================================================
# NEW USER
# =========================================================

def notify_new_user():

    return send_admin_notification(
        event_type="new_user",
        message="A new user registered on Toolora."
    )


# =========================================================
# PRO SUBSCRIPTION
# =========================================================

def notify_new_subscription():

    return send_admin_notification(
        event_type="new_subscription",
        message="A new Toolora Pro subscription was created."
    )


# =========================================================
# PAYMENT SUCCESS
# =========================================================

def notify_payment_success(
    amount: int,
    currency: str = "usd"
):

    return send_admin_notification(
        event_type="payment_success",
        message=(
            f"Successful payment received: "
            f"{amount / 100:.2f} {currency.upper()}."
        )
    )


# =========================================================
# PAYMENT FAILED
# =========================================================

def notify_payment_failed():

    return send_admin_notification(
        event_type="payment_failed",
        message="A Toolora subscription payment failed."
    )


# =========================================================
# SUBSCRIPTION CANCELED
# =========================================================

def notify_subscription_canceled():

    return send_admin_notification(
        event_type="subscription_canceled",
        message="A Toolora Pro subscription was canceled."
    )


# =========================================================
# SYSTEM ERROR
# =========================================================

def notify_system_error(
    error_message: str
):

    # Avoid sending sensitive/private information.
    safe_message = str(error_message)[:500]

    return send_admin_notification(
        event_type="system_error",
        message=f"Toolora system error: {safe_message}"
    )


# =========================================================
# ADMIN TEST ENDPOINT
# =========================================================

@router.post("/test")
async def test_admin_notification():

    success = send_admin_notification(
        event_type="test",
        message="Toolora admin notifications are working."
    )

    if not success:

        raise HTTPException(
            status_code=503,
            detail="Admin notifications are disabled."
        )

    return {
        "success": True,
        "message": "Test notification created."
    }
