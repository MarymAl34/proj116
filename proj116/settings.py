from pathlib import Path
from django.utils.translation import gettext_lazy as _

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح الأمان (❗يجب عدم مشاركته في الإنتاج)
SECRET_KEY = 'django-insecure-i999%anm4i4-5*%1ead2vx#3kfa-igo86t+5_(20-m*pz(p5jh'

# وضع التصحيح (❗أغلقه في الإنتاج)
DEBUG = True

ALLOWED_HOSTS = []

# التطبيقات المثبتة
INSTALLED_APPS = [
    # تطبيقات Django الأساسية
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # التطبيقات المخصصة
    'accounts',
    'store',
    'payments',
]

# الوسطاء
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # ✅ لدعم الترجمة
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ملفات الراوت
ROOT_URLCONF = 'proj116.urls'

# إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # مجلد القوالب العام
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # مهم لـ LoginView
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# تطبيق WSGI
WSGI_APPLICATION = 'proj116.wsgi.application'

# قاعدة البيانات (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# التحقق من كلمات المرور
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# تخصيص نموذج المستخدم
AUTH_USER_MODEL = 'accounts.CustomUser'

# ✅ إعدادات اللغة والتوقيت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# ✅ دعم ملفات الترجمة (اختياري إن رغبتِ بملفات po/mo)
LANGUAGES = [
    ('ar', _('العربية')),
    ('en', _('الإنجليزية')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# الملفات الثابتة
STATIC_URL = '/static/'

# نوع الحقل الافتراضي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ إعدادات تسجيل الدخول والعودة بعده
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
