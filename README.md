# 🛠️ Toolora - Online Tools Platform

Toolora یک پلتفرم SaaS حرفه‌ای برای ابزارهای آنلاین مفید است.

## ✨ ویژگی‌ها

- **Word Counter** - شمارش تعداد کلمات متن
- **Character Counter** - شمارش تعداد کاراکترها
- **Text Cleaner** - پاک‌کردن و تمیز‌کردن متن
- **JSON Formatter** - فرمت‌بندی و اعتبارسنجی JSON

## 🎯 ویژگی‌های پروژه

✅ صفحه اصلی حرفه‌ای
✅ صفحات اختصاصی برای هر ابزار
✅ طراحی Responsive (موبایل و کامپیوتر)
✅ Backend واقعی با Python و FastAPI
✅ ساختار مرتب و قابل توسعه
✅ آماده برای اضافه کردن ابزارهای جدید

## 🚀 نصب و راه‌اندازی

### پیش‌نیازها
- Python 3.8 یا بالاتر
- pip (مدیریت بسته‌های Python)

### مراحل نصب

1. **مخزن را Clone کنید:**
```bash
git clone https://github.com/aryanjahanbakhsh333-ux/Toolora.git
cd Toolora
```

2. **محیط مجازی ایجاد کنید:**
```bash
python -m venv venv
```

3. **محیط مجازی را فعال کنید:**

**برای Windows:**
```bash
venv\Scripts\activate
```

**برای Mac/Linux:**
```bash
source venv/bin/activate
```

4. **وابستگی‌ها را نصب کنید:**
```bash
pip install -r requirements.txt
```

5. **سرور را اجرا کنید:**
```bash
python run.py
```

6. **مرورگر را باز کنید:**
```
http://localhost:8000
```

## 📁 ساختار پروژه

```
Toolora/
├── app/
│   ├── __init__.py
│   ├── main.py              # نقطه اصلی FastAPI
│   ├── models.py            # مدل‌های پایگاه داده
│   ├── database.py          # تنظیمات پایگاه داده
│   ├── tools/               # منطق ابزارها
│   │   ├── __init__.py
│   │   ├── word_counter.py
│   │   ├── character_counter.py
│   │   ├── text_cleaner.py
│   │   └── json_formatter.py
│   └── routes/              # مسیرهای API
│       ├── __init__.py
│       └── tools.py
├── static/
│   ├── css/
│   │   ├── style.css        # استایل‌های اصلی
│   │   └── responsive.css   # استایل‌های responsive
│   └── js/
│       └── main.js          # اسکریپت‌های جاوااسکریپت
├── templates/
│   ├── base.html            # قالب پایه
│   ├── index.html           # صفحه اصلی
│   ├── tools/
│   │   ├── word_counter.html
│   │   ├── character_counter.html
│   │   ├── text_cleaner.html
│   │   └── json_formatter.html
│   └── error.html           # صفحه خطا
├── requirements.txt         # وابستگی‌های پروژه
├── run.py                   # اجرای برنامه
└── README.md                # این فایل

```

## 🛠️ نحوه استفاده

1. صفحه اصلی را باز کنید
2. یکی از ابزارها را انتخاب کنید
3. متن یا کد خود را وارد کنید
4. نتیجه فوری را مشاهده کنید

## 🔧 توسعه و اضافه کردن ابزارهای جدید

برای اضافه کردن یک ابزار جدید:

1. یک فایل جدید در `app/tools/` بسازید
2. منطق ابزار را پیاده‌سازی کنید
3. یک route در `app/routes/tools.py` اضافه کنید
4. یک template در `templates/tools/` ایجاد کنید
5. لینک را به صفحه اصلی اضافه کنید

## 📝 نکات برنامه‌نویسی

- **FastAPI**: برای backend و API
- **SQLAlchemy**: برای مدیریت پایگاه داده
- **Jinja2**: برای rendering HTML templates
- **SQLite**: برای ذخیره داده‌ها
- **HTML/CSS/JavaScript**: برای frontend

## 📄 لایسنس

MIT License

## 👨‍💻 توسعه‌دهنده

ایجاد شده توسط GitHub Copilot

---

**برای کمک یا پیشنهادات، issue را باز کنید!** 🎉
