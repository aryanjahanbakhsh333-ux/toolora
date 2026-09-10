"""ابزار شمارش کاراکترها"""

def count_characters(text: str) -> dict:
    """
    شمارش تعداد کاراکترها و تحلیل متن
    
    Args:
        text: متن ورودی
    
    Returns:
        dict: شامل تحلیل کاراکترها
    """
    if not text:
        return {
            "total_chars": 0,
            "chars_without_spaces": 0,
            "spaces": 0,
            "digits": 0,
            "letters": 0,
            "uppercase_letters": 0,
            "lowercase_letters": 0,
            "special_chars": 0,
            "newlines": 0
        }
    
    total_chars = len(text)
    chars_without_spaces = len(text.replace(" ", ""))
    spaces = text.count(" ")
    digits = sum(1 for c in text if c.isdigit())
    letters = sum(1 for c in text if c.isalpha())
    uppercase_letters = sum(1 for c in text if c.isupper())
    lowercase_letters = sum(1 for c in text if c.islower())
    newlines = text.count("\n")
    special_chars = total_chars - spaces - digits - letters - newlines
    
    return {
        "total_chars": total_chars,
        "chars_without_spaces": chars_without_spaces,
        "spaces": spaces,
        "digits": digits,
        "letters": letters,
        "uppercase_letters": uppercase_letters,
        "lowercase_letters": lowercase_letters,
        "special_chars": special_chars,
        "newlines": newlines
    }
