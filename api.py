from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/api", tags=["Mobile API"])


# =========================
# Response Models
# =========================

class UserResponse(BaseModel):
    id: int
    email: str
    plan: str


class ToolResponse(BaseModel):
    name: str
    slug: str
    available: bool


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


# =========================
# API Health Check
# =========================

@router.get("/health", response_model=HealthResponse)
async def health_check():
    return {
        "status": "ok",
        "service": "Toolora API",
        "version": "1.0.0"
    }


# =========================
# Available Tools
# =========================

@router.get("/tools", response_model=list[ToolResponse])
async def get_tools():

    return [
        {
            "name": "AI Text Rewriter",
            "slug": "rewriter",
            "available": True
        },
        {
            "name": "AI Summarizer",
            "slug": "summarizer",
            "available": True
        },
        {
            "name": "AI Email Writer",
            "slug": "email-writer",
            "available": True
        },
        {
            "name": "Grammar Improver",
            "slug": "grammar",
            "available": True
        },
        {
            "name": "Word Counter",
            "slug": "word-counter",
            "available": True
        },
        {
            "name": "Character Counter",
            "slug": "character-counter",
            "available": True
        },
        {
            "name": "Text Cleaner",
            "slug": "text-cleaner",
            "available": True
        },
        {
            "name": "JSON Formatter",
            "slug": "json-formatter",
            "available": True
        }
    ]


# =========================
# App Configuration
# =========================

@router.get("/config")
async def app_config():

    return {
        "app_name": "Toolora",
        "version": "1.0.0",
        "minimum_app_version": "1.0.0",
        "website": "https://your-domain.com",
        "support_email": "support@your-domain.com",
        "features": {
            "authentication": True,
            "subscriptions": True,
            "payments": True,
            "history": True,
            "ai_tools": True
        }
    }


# =========================
# Subscription Status
# =========================

@router.get("/subscription")
async def subscription_status():

    # این قسمت بعداً به سیستم واقعی
    # Subscription وصل می‌شود.

    return {
        "plan": "free",
        "status": "active",
        "pro": False
    }
