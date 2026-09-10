"""ابزار شمارش کلمات"""

def count_words(text: str) -> dict:
    """
    شمارش تعداد کلمات متن
    
    Args:
        text: متن ورودی
    
    Returns:
        dict: شامل تعداد کلمات و اطلاعات بیشتر
    """
    if not text or not text.strip():
        return {
            "word_count": 0,
            "char_count": 0,
            "char_count_without_spaces": 0,
            "line_count": 0,
            "paragraph_count": 0,
            "average_word_length": 0
        }
    
    # شمارش کلمات
    words = text.split()
    word_count = len(words)
    
    # شمارش کاراکترها
    char_count = len(text)
    char_count_without_spaces = len(text.replace(" ", ""))
    
    # شمارش خطوط
    lines = text.split("\n")
    line_count = len([line for line in lines if line.strip()])
    
    # شمارش پاراگراف‌ها
    paragraphs = text.split("\n\n")
    paragraph_count = len([p for p in paragraphs if p.strip()])
    
    # میانگین طول کلمات
    average_word_length = round(char_count_without_spaces / word_count, 2) if word_count > 0 else 0
    
    return {
        "word_count": word_count,
        "char_count": char_count,
        "char_count_without_spaces": char_count_without_spaces,
        "line_count": line_count,
        "paragraph_count": paragraph_count,
        "average_word_length": average_word_length
    }
