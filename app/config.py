# Toolora - Online Tools Platform
# Multi-language Configuration

LANGUAGES = {
    'fa': {
        'name': 'فارسی',
        'direction': 'rtl',
        'flag': '🇮🇷'
    },
    'de': {
        'name': 'Deutsch',
        'direction': 'ltr',
        'flag': '🇩🇪'
    },
    'he': {
        'name': 'עברית',
        'direction': 'rtl',
        'flag': '🇮🇱'
    },
    'en': {
        'name': 'English',
        'direction': 'ltr',
        'flag': '🇺🇸'
    }
}

# Translations Dictionary
TRANSLATIONS = {
    'fa': {
        'home': 'خانه',
        'tools': 'ابزارها',
        'about': 'درباره',
        'privacy': 'حریم خصوصی',
        'terms': 'شرایط',
        'welcome': 'خوش آمدید به Toolora',
        'description': 'پلتفرم جامع ابزارهای آنلاین برای تمام نیاز‌های شما',
        'start': 'شروع کنید',
        'word_counter': 'شمارش کلمات',
        'character_counter': 'شمارش کا��اکترها',
        'text_cleaner': 'پاک‌کنندگی متن',
        'json_formatter': 'فرمت‌کننده JSON',
        'about_us': 'درباره ما',
        'contact': 'تماس با ما',
        'rights': 'تمام حقوق محفوظ است',
        'made_with': 'ساخته شده با Python و FastAPI',
    },
    'de': {
        'home': 'Startseite',
        'tools': 'Werkzeuge',
        'about': 'Über uns',
        'privacy': 'Datenschutz',
        'terms': 'Bedingungen',
        'welcome': 'Willkommen bei Toolora',
        'description': 'Eine umfassende Plattform mit Online-Tools für alle Ihre Anforderungen',
        'start': 'Jetzt starten',
        'word_counter': 'Wörter zählen',
        'character_counter': 'Zeichen zählen',
        'text_cleaner': 'Text-Reiniger',
        'json_formatter': 'JSON-Formatierer',
        'about_us': 'Über uns',
        'contact': 'Kontaktieren Sie uns',
        'rights': 'Alle Rechte vorbehalten',
        'made_with': 'Erstellt mit Python und FastAPI',
    },
    'he': {
        'home': 'בית',
        'tools': 'כלים',
        'about': 'אודות',
        'privacy': 'פרטיות',
        'terms': 'תנאים',
        'welcome': 'ברוכים הבאים ל-Toolora',
        'description': 'פלטפור��ה מקיפה של כלים מקוונים לכל הצרכים שלך',
        'start': 'התחל עכשיו',
        'word_counter': 'ספירת מילים',
        'character_counter': 'ספירת תווים',
        'text_cleaner': 'מנקה טקסט',
        'json_formatter': 'פורמטר JSON',
        'about_us': 'אודות',
        'contact': 'צור קשר',
        'rights': 'כל הזכויות שמורות',
        'made_with': 'נבנה עם Python ו-FastAPI',
    },
    'en': {
        'home': 'Home',
        'tools': 'Tools',
        'about': 'About',
        'privacy': 'Privacy',
        'terms': 'Terms',
        'welcome': 'Welcome to Toolora',
        'description': 'A comprehensive platform of online tools for all your needs',
        'start': 'Get Started',
        'word_counter': 'Word Counter',
        'character_counter': 'Character Counter',
        'text_cleaner': 'Text Cleaner',
        'json_formatter': 'JSON Formatter',
        'about_us': 'About Us',
        'contact': 'Contact Us',
        'rights': 'All rights reserved',
        'made_with': 'Made with Python and FastAPI',
    }
}

def get_translation(language: str, key: str, default: str = None) -> str:
    """Get translation for a key in a specific language"""
    if language not in TRANSLATIONS:
        language = 'en'
    
    translation = TRANSLATIONS[language].get(key)
    return translation if translation else (default or key)
