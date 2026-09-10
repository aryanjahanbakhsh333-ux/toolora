"""ابزار فرمت‌بندی JSON"""

import json
from typing import Any

def validate_json(json_string: str) -> dict:
    """
    اعتبارسنجی JSON
    
    Args:
        json_string: رشته JSON
    
    Returns:
        dict: شامل وضعیت صحت‌سنجی و پیام‌ها
    """
    try:
        json.loads(json_string)
        return {
            "valid": True,
            "error": None,
            "message": "JSON معتبر است"
        }
    except json.JSONDecodeError as e:
        return {
            "valid": False,
            "error": str(e),
            "message": f"خطای JSON: {str(e)}"
        }

def format_json(json_string: str, indent: int = 2, sort_keys: bool = False) -> dict:
    """
    فرمت‌بندی JSON با فاصله‌های صحیح
    
    Args:
        json_string: رشته JSON
        indent: تعداد فاصله‌ها برای indentation
        sort_keys: مرتب‌سازی کلیدها
    
    Returns:
        dict: شامل JSON فرمت‌شده یا خطا
    """
    try:
        # Parse JSON
        parsed = json.loads(json_string)
        
        # Format JSON
        formatted = json.dumps(
            parsed,
            indent=indent,
            ensure_ascii=False,
            sort_keys=sort_keys
        )
        
        return {
            "valid": True,
            "formatted": formatted,
            "error": None,
            "message": "JSON با موفقیت فرمت‌شد"
        }
    except json.JSONDecodeError as e:
        return {
            "valid": False,
            "formatted": None,
            "error": str(e),
            "message": f"خطا در فرمت‌کردن JSON: {str(e)}"
        }

def minify_json(json_string: str) -> dict:
    """
    تبدیل JSON به شکل فشرده (بدون فاصله‌های اضافی)
    
    Args:
        json_string: رشته JSON
    
    Returns:
        dict: شامل JSON فشرده یا خطا
    """
    try:
        # Parse JSON
        parsed = json.loads(json_string)
        
        # Minify JSON
        minified = json.dumps(
            parsed,
            separators=(',', ':'),
            ensure_ascii=False
        )
        
        return {
            "valid": True,
            "minified": minified,
            "error": None,
            "message": "JSON با موفقیت فشرده شد"
        }
    except json.JSONDecodeError as e:
        return {
            "valid": False,
            "minified": None,
            "error": str(e),
            "message": f"خطا در فشردن JSON: {str(e)}"
        }
