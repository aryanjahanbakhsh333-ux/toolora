"""FastAPI Application - Toolora"""

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.database import init_db
from app.routes import tools
import os

# Initialize FastAPI app
app = FastAPI(
    title="Toolora",
    description="پلتفرم جامع ابزارهای آنلاین حرفه‌ای",
    version="1.0.0"
)

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "..", "static")
if os.path.exists(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Setup templates
templates_dir = os.path.join(os.path.dirname(__file__), "..", "templates")
templates = Jinja2Templates(directory=templates_dir)

# Initialize database
init_db()

# Include routes
app.include_router(tools.router)

# Home page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """صفحه اصلی"""
    return templates.TemplateResponse("index.html", {"request": request})

# About page
@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    """صفحه درباره Toolora"""
    return templates.TemplateResponse("about.html", {"request": request})

# Privacy Policy page
@app.get("/privacy", response_class=HTMLResponse)
async def privacy_page(request: Request):
    """صفحه سیاست حریم خصوصی"""
    return templates.TemplateResponse("privacy.html", {"request": request})

# Terms of Service page
@app.get("/terms", response_class=HTMLResponse)
async def terms_page(request: Request):
    """صفحه شرایط استفاده"""
    return templates.TemplateResponse("terms.html", {"request": request})

# Word Counter page
@app.get("/word-counter", response_class=HTMLResponse)
async def word_counter_page(request: Request):
    """صفحه شمارش کلمات"""
    return templates.TemplateResponse("tools/word_counter.html", {"request": request})

# Character Counter page
@app.get("/character-counter", response_class=HTMLResponse)
async def character_counter_page(request: Request):
    """صفحه شمارش کاراکترها"""
    return templates.TemplateResponse("tools/character_counter.html", {"request": request})

# Text Cleaner page
@app.get("/text-cleaner", response_class=HTMLResponse)
async def text_cleaner_page(request: Request):
    """صفحه پاک‌کنندگی متن"""
    return templates.TemplateResponse("tools/text_cleaner.html", {"request": request})

# JSON Formatter page
@app.get("/json-formatter", response_class=HTMLResponse)
async def json_formatter_page(request: Request):
    """صفحه فرمت‌کنندهی JSON"""
    return templates.TemplateResponse("tools/json_formatter.html", {"request": request})

# Tools listing page (optional)
@app.get("/tools", response_class=HTMLResponse)
async def tools_page(request: Request):
    """صفحه لیست ابزارها"""
    return templates.TemplateResponse("index.html", {"request": request})

# Health check
@app.get("/health")
async def health_check():
    """بررسی وضعیت سرویس"""
    return {
        "status": "ok",
        "message": "Toolora is running perfectly!"
    }

# 404 Error handler
@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    """مدیریت خطای 404"""
    return templates.TemplateResponse(
        "error.html",
        {"request": request, "error": "صفحه مورد نظر یافت نشد"},
        status_code=404
    )

# Root API documentation
@app.get("/api/docs", include_in_schema=False)
async def api_docs():
    """مستندات API"""
    return {
        "api_version": "1.0.0",
        "endpoints": {
            "word_counter": "/api/word-counter",
            "character_counter": "/api/character-counter",
            "text_cleaner": "/api/text-cleaner",
            "json_formatter": "/api/json-formatter",
            "health": "/api/health"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
