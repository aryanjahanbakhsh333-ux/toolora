# 🛠️ Toolora - Platform ابزارهای آنلاین

**نسخه:** 1.0.0  
**زبان:** Python 3.8+  
**Framework:** FastAPI

---

## 📋 فهرست محتوا

- [درباره پروژه](#درباره-پروژه)
- [نسخه‌های موجود](#نسخه‌های-موجود)
- [نیازمندی‌های سیستم](#نیازمندی‌های-سیستم)
- [نصب و راه‌اندازی](#نصب-و-راه‌اندازی)
- [اجرای برنامه](#اجرای-برنامه)
- [ساختار پروژه](#ساختار-پروژه)
- [استفاده از ابزارها](#استفاده-از-ابزارها)
- [توسعه و اضافه‌کردن ابزارهای جدید](#توسعه-و-اضافه‌کردن-ابزارهای-جدید)
- [API مستندات](#api-مستندات)
- [راهنمای بیشتر](#راهنمای-بیشتر)

---

## 🎯 درباره پروژه

**Toolora** یک سایت SaaS حرفه‌ای است که مجموعه‌ای از ابزارهای کاربردی آنلاین را فراهم می‌کند.

### ویژگی‌های اصلی:
✅ رابط کاربری ساده و زیبا  
✅ طراحی Responsive (موبایل و کامپیوتر)  
✅ API واقعی و قابل استفاده  
✅ پایگاه داده SQLite  
✅ کد مرتب و قابل توسعه  
✅ بدون نیاز به نصب پیچیده  

---

## 📦 نسخه‌های موجود

### نسخه 1.0.0 (فعلی)

1. **Word Counter** - شمارش کلمات، کاراکترها، خطوط و پاراگراف‌ها
2. **Character Counter** - تحلیل کاراکترها (حروف، اعداد، علائم)
3. **Text Cleaner** - پاک‌کردن متن (حذف فاصله‌های اضافی، علائم خاص، تبدیل حروف)
4. **JSON Formatter** - فرمت‌بندی، اعتبار‌سنجی و فشرده‌سازی JSON

---

## 🖥️ نیازمندی‌های سیستم

### نرم‌افزاری:
- **Python 3.8** یا بالاتر
- **pip** (مدیریت بسته‌های Python)
- **Git** (اختیاری برای Clone کردن)

### سخت‌افزاری:
- حداقل **512 MB** RAM
- حداقل **100 MB** فضای آزاد
- اتصال اینترنت برای دانلود وابستگی‌ها

---

## 🚀 نصب و راه‌اندازی

### مرحله 1: Clone کردن مخزن

```bash
git clone https://github.com/aryanjahanbakhsh333-ux/Toolora.git
cd Toolora
```

### مرحله 2: ایجاد محیط مجازی

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### مرحله 3: نصب وابستگی‌ها

```bash
pip install -r requirements.txt
```

**اگر خطا دریافت کردید:**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## ▶️ اجرای برنامه

### روش 1: استفاده از run.py (آسان‌تر)

```bash
python run.py
```

### روش 2: استفاده از uvicorn مستقیم

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### مرحله آخر: باز کردن مرورگر

```
http://localhost:8000
```

**نکات:**
- سرور خودکار بند می‌شود با Ctrl + C
- اگر پورت 8000 اشغال است، می‌توانید آن را تغییر دهید:
  ```bash
  python run.py --port 8001
  ```

---

## 📁 ساختار پروژه

```
Toolora/
├── app/
│   ├── __init__.py
│   ├── main.py                 # نقطه ورود FastAPI
│   ├── database.py             # تنظیمات پایگاه داده
│   ├── models.py               # مدل‌های پایگاه داده
│   ├── tools/                  # منطق ابزارها
│   │   ├── __init__.py
│   │   ├── word_counter.py
│   │   ├── character_counter.py
│   │   ├── text_cleaner.py
│   │   └── json_formatter.py
│   └── routes/                 # مسیرهای API
│       ├── __init__.py
│       └── tools.py
├── static/                     # فایل‌های استاتیک
│   ├── css/
│   │   ├── style.css          # استایل‌های اصلی
│   │   └── responsive.css     # استایل‌های پاسخ‌گو
│   └── js/
│       └── main.js            # اسکریپت‌های اصلی
├── templates/                  # فایل‌های HTML
│   ├── base.html              # قالب پایه
│   ├── index.html             # صفحه اصلی
│   ├── error.html             # صفحه خطا
│   └── tools/
│       ├── word_counter.html
│       ├── character_counter.html
│       ├── text_cleaner.html
│       └── json_formatter.html
├── requirements.txt            # وابستگی‌های Python
├── run.py                      # فایل اجرای پروژه
├── README.md                   # این فایل
└── .gitignore                 # فایل‌های نادیده در Git
```

---

## 🎯 استفاده از ابزارها

### 1️⃣ Word Counter

**برای چه استفاده می‌شود:**
- شمارش کلمات و کاراکترها
- محاسبه میانگین طول کلمات
- تحلیل متن برای نویسندگان و بلاگرها

**نحوه استفاده:**
1. به صفحه `/word-counter` بروید
2. متن خود را وارد کنید
3. دکمه "شمارش" را کلیک کنید
4. نتایج فوری نمایش داده می‌شود

---

### 2️⃣ Character Counter

**برای چه استفاده می‌شود:**
- تحلیل تفصیلی کاراکترها
- شمارش اعداد و حروف
- حساب‌کردن علائم و کاراکترهای خاص

**نحوه استفاده:**
1. به صفحه `/character-counter` بروید
2. متن را وارد کنید
3. دکمه "تحلیل" را کلیک کنید

---

### 3️⃣ Text Cleaner

**برای چه استفاده می‌شود:**
- پاک‌کردن متن از فاصله‌های اضافی
- حذف خطوط خالی
- تبدیل حروف (بزرگ/کوچک)

**گزینه‌های موجود:**
- ☑️ حذف فاصله‌های اضافی
- ☑️ حذف خطوط خالی
- ☑️ حذف کاراکترهای خاص
- ☑️ تبدیل به حروف کوچک
- ☑️ تبدیل به حروف بزرگ
- ☑️ حذف فاصله از شروع و انتها

---

### 4️⃣ JSON Formatter

**برای چه استفاده می‌شود:**
- فرمت‌بندی JSON
- اعتبار‌سنجی JSON
- فشرده‌سازی JSON

**گزینه‌های موجود:**
- **Format**: فرمت‌بندی زیبا
- **Minify**: حذف فاصله‌های اضافی
- **Validate**: بررسی صحت

---

## 🔧 توسعه و اضافه‌کردن ابزارهای جدید

### مثال: اضافه‌کردن ابزار جدید "Text to Uppercase"

#### گام 1: ایجاد فایل منطق

فایل `app/tools/text_to_uppercase.py`:

```python
def convert_to_uppercase(text: str) -> str:
    """تبدیل متن به حروف بزرگ"""
    return text.upper()
```

#### گام 2: اضافه‌کردن Route

در فایل `app/routes/tools.py` اضافه کنید:

```python
from app.tools import text_to_uppercase

@router.post("/text-to-uppercase")
async def api_text_to_uppercase(request: dict, db: Session = Depends(get_db)):
    result = text_to_uppercase.convert_to_uppercase(request.get("text", ""))
    return {"result": result}
```

#### گام 3: ایجاد Template

فایل `templates/tools/text_to_uppercase.html`:

```html
{% extends "base.html" %}
{% block title %}Text to Uppercase{% endblock %}
{% block content %}
<!-- کد HTML اینجا -->
{% endblock %}
```

#### گام 4: اضافه‌کردن لینک

در `templates/index.html` به بخش tools-grid اضافه کنید:

```html
<div class="tool-card">
    <div class="tool-icon">📝</div>
    <h3>تبدیل به بزرگ</h3>
    <p>تبدیل تمام حروف به بزرگ</p>
    <a href="/text-to-uppercase" class="btn btn-secondary">استفاده کنید</a>
</div>
```

---

## 📡 API مستندات

### Word Counter API

**Endpoint:** `POST /api/word-counter`

**Request:**
```json
{
    "text": "مثال متن برای شمارش"
}
```

**Response:**
```json
{
    "word_count": 4,
    "char_count": 22,
    "char_count_without_spaces": 18,
    "line_count": 1,
    "paragraph_count": 1,
    "average_word_length": 4.5
}
```

---

### Character Counter API

**Endpoint:** `POST /api/character-counter`

**Response:**
```json
{
    "total_chars": 22,
    "chars_without_spaces": 18,
    "spaces": 4,
    "digits": 0,
    "letters": 18,
    "uppercase_letters": 0,
    "lowercase_letters": 18,
    "special_chars": 0,
    "newlines": 0
}
```

---

### Text Cleaner API

**Endpoint:** `POST /api/text-cleaner`

**Request:**
```json
{
    "text": "متن    دارای   فاصله اضافی",
    "remove_extra_spaces": true,
    "remove_empty_lines": false,
    "lowercase": false,
    "uppercase": false,
    "trim": true
}
```

**Response:**
```json
{
    "cleaned_text": "متن دارای فاصله اضافی"
}
```

---

### JSON Formatter API

**Endpoint:** `POST /api/json-formatter`

**Request:**
```json
{
    "json_string": "{\"name\":\"test\"}",
    "action": "format",
    "indent": 2,
    "sort_keys": false
}
```

**Response (success):**
```json
{
    "valid": true,
    "formatted": "{\n  \"name\": \"test\"\n}",
    "error": null,
    "message": "JSON با موفقیت فرمت‌شد"
}
```

**Response (error):**
```json
{
    "valid": false,
    "formatted": null,
    "error": "Expecting value: line 1 column 1",
    "message": "خطای JSON: Expecting value..."
}
```

---

## 📱 Responsive Design

سایت Toolora به طور کامل Responsive است:

- **Desktop** (1200px+): تمام ویژگی‌ها
- **Tablet** (768px-1199px): قالب دو ستونی
- **Mobile** (480px-767px): قالب یک ستونی
- **Extra Small** (زیر 480px): بهینه‌شده برای صفحات کوچک

---

## 🔐 نکات امنیتی

⚠️ **مهم:** قبل از استقرار در تولید:

1. متغیرهای محیطی را تنظیم کنید
2. SECRET_KEY را تغییر دهید
3. DEBUG را OFF کنید
4. CORS را محدود کنید
5. HTTPS را فعال کنید

---

## 🐛 رفع مشکلات عام

### مشکل: Port 8000 قبلاً استفاده شده است

**راه حل:**
```bash
# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux
lsof -i :8000
kill -9 <PID>
```

### مشکل: خطای Import

**راه حل:**
```bash
pip install -r requirements.txt
```

### مشکل: پایگاه داده خراب

**راه حل:**
```bash
# حذف فایل پایگاه داده
rm toolora.db
# اجرا مجدد برنامه
python run.py
```

---

## 📚 منابع مفید

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://www.sqlalchemy.org/)
- [Jinja2 Templates](https://jinja.palletsprojects.com/)

---

## 📝 لایسنس

MIT License - آزادانه استفاده کنید!

---

## 👨‍💻 توسعه‌دهنده

ساخته شده توسط **GitHub Copilot** برای شما ❤️

---

**سوالات یا مشکلات؟** Issues را باز کنید یا تماس بگیرید!

🌟 اگر از این پروژه لذت بردید، ستاره بدهید!
