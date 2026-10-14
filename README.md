# Facebook Django | فیس‌بوک جنگو

<div dir="rtl">

## 🇮🇷 فارسی

### 📖 درباره پروژه

یک شبکه اجتماعی فارسی شبیه فیسبوک که با **Django** ساخته شده. کاربران می‌توانند ثبت‌نام کنند، پست بسازند، ویرایش و حذف کنند، لایک بزنند و کامنت بگذارند.

### ✨ امکانات

- ✅ ثبت‌نام و ورود کاربران
- ✅ ساخت پست با عکس
- ✅ ویرایش و حذف پست
- ✅ لایک کردن پست‌ها
- ✅ کامنت گذاشتن روی پست‌ها
- ✅ حالت شب و روز (Dark/Light Mode)
- ✅ طراحی واکنش‌گرا (Responsive)
- ✅ پشتیبانی از RTL
- ✅ لودر سراسری
- ✅ امنیت با `.env`

### 🛠 تکنولوژی‌ها

- **Backend**: Django 6.0, Python 3.12
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Database**: SQLite3
- **Config**: python-dotenv
- **Version Control**: Git

### 🚀 نصب و راه‌اندازی

#### پیش‌نیازها
- Python 3.12 یا بالاتر
- Git

#### مراحل نصب

۱. Clone کردن پروژه:
```bash
git clone https://github.com/mmdbyrnwn-lgtm/facebook_django.git
cd facebook_django
```

۲. ساخت محیط مجازی:
```bash
python -m venv venv
```

۳. فعال‌سازی محیط مجازی:
```bash
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

۴. نصب پکیج‌های مورد نیاز:
```bash
pip install -r requirements.txt
```

۵. ساخت فایل `.env` در ریشه پروژه:
```
SECRET_KEY=your-secret-key-here
```

برای ساخت کلید امن:
```bash
python -c "import secrets, string; print(''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(50)))"
```

۶. اجرای migrationها:
```bash
python manage.py migrate
```

۷. ساخت ادمین:
```bash
python manage.py createsuperuser
```

۸. اجرای سرور:
```bash
python manage.py runserver
```

۹. باز کردن در مرورگر:
```
http://127.0.0.1:8000/
```

### 📁 ساختار پروژه

```
facebook_django/
├── accounts/              # اپ مدیریت کاربران
├── core/                  # اپ اصلی (پست، کامنت، لایک)
│   ├── static/            # فایل‌های استاتیک
│   ├── templates/         # قالب‌های HTML
│   ├── models.py          # مدل‌های دیتابیس
│   ├── views.py           # منطق برنامه
│   └── urls.py            # مسیرها
├── facebook/              # تنظیمات اصلی پروژه
│   ├── settings.py
│   └── urls.py
├── media/                 # فایل‌های آپلودی (در Git نیست)
├── manage.py
├── requirements.txt
├── .env                   # متغیرهای محیطی (در Git نیست)
└── .gitignore
```

### 🔐 امنیت

- `SECRET_KEY` در فایل `.env` ذخیره می‌شود (نه در Git)
- فایل `.env` در `.gitignore` قرار دارد
- `DEBUG = True` فقط در محیط توسعه

### 👨‍💻 سازنده

**Amirhossein Fallahnejad** ([@amircayto](https://github.com/mmdbyrnwn-lgtm))

### 📝 لایسنس

این پروژه تحت لایسنس **MIT** منتشر شده. استفاده و تغییر آزاد است.

---

</div>

<div dir="ltr">

## 🇬🇧 English

### 📖 About

A Persian social network similar to Facebook, built with **Django**. Users can sign up, create posts, edit and delete them, like posts, and leave comments.

### ✨ Features

- ✅ User registration and login
- ✅ Create posts with images
- ✅ Edit and delete posts
- ✅ Like posts
- ✅ Comment on posts
- ✅ Dark / Light mode
- ✅ Responsive design
- ✅ RTL support
- ✅ Global page loader
- ✅ Security with `.env`

### 🛠 Tech Stack

- **Backend**: Django 6.0, Python 3.12
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite3
- **Config**: python-dotenv
- **Version Control**: Git

### 🚀 Installation

#### Requirements
- Python 3.12+
- Git

#### Setup Steps

1. Clone the repository:
```bash
git clone https://github.com/mmdbyrnwn-lgtm/facebook_django.git
cd facebook_django
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the environment:
```bash
# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the project root:
```
SECRET_KEY=your-secret-key-here
```

Generate a secure key:
```bash
python -c "import secrets, string; print(''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(50)))"
```

6. Run migrations:
```bash
python manage.py migrate
```

7. Create a superuser:
```bash
python manage.py createsuperuser
```

8. Run the development server:
```bash
python manage.py runserver
```

9. Open in your browser:
```
http://127.0.0.1:8000/
```

### 📁 Project Structure

```
facebook_django/
├── accounts/              # User management app
├── core/                  # Main app (posts, comments, likes)
│   ├── static/            # Static files (CSS, JS, images)
│   ├── templates/         # HTML templates
│   ├── models.py          # Database models
│   ├── views.py           # Application logic
│   └── urls.py            # URL routing
├── facebook/              # Project settings
│   ├── settings.py
│   └── urls.py
├── media/                 # User uploads (not in Git)
├── manage.py
├── requirements.txt
├── .env                   # Environment variables (not in Git)
└── .gitignore
```

### 🔐 Security

- `SECRET_KEY` is stored in `.env` (not in Git)
- `.env` file is listed in `.gitignore`
- `DEBUG = True` only for development

### 👨‍💻 Author

**Amirhossein Fallahnejad** ([@amircayto](https://github.com/mmdbyrnwn-lgtm))

### 📝 License

This project is licensed under the **MIT** License. Free to use and modify.

</div>
