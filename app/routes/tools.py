"""مسیرهای API برای ابزارها"""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import ToolUsage
from app.tools import word_counter, character_counter, text_cleaner, json_formatter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/api", tags=["tools"])

# Pydantic Models
class WordCountRequest(BaseModel):
    text: str

class CharacterCountRequest(BaseModel):
    text: str

class TextCleanerRequest(BaseModel):
    text: str
    remove_extra_spaces: bool = False
    remove_empty_lines: bool = False
    remove_special_chars: bool = False
    lowercase: bool = False
    uppercase: bool = False
    trim: bool = False

class JsonFormatterRequest(BaseModel):
    json_string: str
    action: str = "format"  # format, minify, validate
    indent: int = 2
    sort_keys: bool = False

# Word Counter API
@router.post("/word-counter")
async def api_word_counter(request: WordCountRequest, db: Session = Depends(get_db)):
    """API برای شمارش کلمات"""
    result = word_counter.count_words(request.text)
    
    # ثبت استفاده
    usage = ToolUsage(
        tool_name="word_counter",
        input_data=request.text[:500],  # ذخیره اولین 500 کاراکتر
        output_data=str(result)
    )
    db.add(usage)
    db.commit()
    
    return result

# Character Counter API
@router.post("/character-counter")
async def api_character_counter(request: CharacterCountRequest, db: Session = Depends(get_db)):
    """API برای شمارش کاراکترها"""
    result = character_counter.count_characters(request.text)
    
    # ثبت استفاده
    usage = ToolUsage(
        tool_name="character_counter",
        input_data=request.text[:500],
        output_data=str(result)
    )
    db.add(usage)
    db.commit()
    
    return result

# Text Cleaner API
@router.post("/text-cleaner")
async def api_text_cleaner(request: TextCleanerRequest, db: Session = Depends(get_db)):
    """API برای پاک‌کردن متن"""
    options = {
        "remove_extra_spaces": request.remove_extra_spaces,
        "remove_empty_lines": request.remove_empty_lines,
        "remove_special_chars": request.remove_special_chars,
        "lowercase": request.lowercase,
        "uppercase": request.uppercase,
        "trim": request.trim
    }
    
    result = text_cleaner.clean_text(request.text, options)
    
    # ثبت استفاده
    usage = ToolUsage(
        tool_name="text_cleaner",
        input_data=request.text[:500],
        output_data=result[:500]
    )
    db.add(usage)
    db.commit()
    
    return {"cleaned_text": result}

# JSON Formatter API
@router.post("/json-formatter")
async def api_json_formatter(request: JsonFormatterRequest, db: Session = Depends(get_db)):
    """API برای فرمت‌بندی JSON"""
    if request.action == "validate":
        result = json_formatter.validate_json(request.json_string)
    elif request.action == "minify":
        result = json_formatter.minify_json(request.json_string)
    else:  # format
        result = json_formatter.format_json(
            request.json_string,
            indent=request.indent,
            sort_keys=request.sort_keys
        )
    
    # ثبت استفاده
    usage = ToolUsage(
        tool_name="json_formatter",
        input_data=request.json_string[:500],
        output_data=str(result)[:500]
    )
    db.add(usage)
    db.commit()
    
    return result

# Health Check
@router.get("/health")
async def health_check():
    """بررسی وضعیت API"""
    return {"status": "ok", "message": "Toolora API is running"}
