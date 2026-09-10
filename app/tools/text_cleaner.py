"""ابزار پاک‌کردن و تمیز‌کردن متن"""

import re

def clean_text(text: str, options: dict) -> str:
    """
    پاک‌کردن و تمیز‌کردن متن بر اساس گزینه‌های انتخاب‌شده
    
    Args:
        text: متن ورودی
        options: گزینه‌های تمیزکاری
            - remove_extra_spaces: حذف فاصله‌های اضافی
            - remove_empty_lines: حذف خطوط خالی
            - remove_special_chars: حذف کاراکترهای خاص
            - lowercase: تبدیل به حروف کوچک
            - uppercase: تبدیل به حروف بزرگ
            - trim: حذف فاصله از ابتدا و انتهای متن
    
    Returns:
        str: متن تمیزشده
    """
    result = text
    
    # حذف فاصله‌های اضافی
    if options.get("remove_extra_spaces", False):
        result = re.sub(r'  +', ' ', result)
    
    # حذف خطوط خالی
    if options.get("remove_empty_lines", False):
        result = "\n".join(line for line in result.split("\n") if line.strip())
    
    # حذف کاراکترهای خاص
    if options.get("remove_special_chars", False):
        result = re.sub(r'[^a-zA-Z0-9\s\n\u0600-\u06FF]', '', result)
    
    # تبدیل به حروف کوچک
    if options.get("lowercase", False):
        result = result.lower()
    
    # تبدیل به حروف بزرگ
    if options.get("uppercase", False):
        result = result.upper()
    
    # حذف فاصله از ابتدا و انتهای متن
    if options.get("trim", False):
        result = result.strip()
    
    return result
