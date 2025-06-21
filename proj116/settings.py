from pathlib import Path
from django.utils.translation import gettext_lazy as _
import cloudinary

# المسار الأساسي للمشروع
BASE_DIR = Path(__file__).resolve().parent.parent

# مفتاح الأمان
SECRET_KEY = 'django-insecure-i999%anm4i4-5*%1ead2vx#3kfa-igo86t+5_(20-m*pz(p5jh'

# وضع التصحيح
DEBUG = True

ALLOWED_HOSTS = []

# التطبيقات المثبتة
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # تطبيقات الطرف الثالث
    'cloudinary',
    'cloudinary_storage',

    # تطبيقات المشروع
    'accounts',
    'store',
    'payments',
]

# الوسطاء
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# إعدادات الراوت
ROOT_URLCONF = 'proj116.urls'

# إعدادات القوالب
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# إعدادات WSGI
WSGI_APPLICATION = 'proj116.wsgi.application'

# قاعدة البيانات
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

# نموذج المستخدم المخصص
AUTH_USER_MODEL = 'accounts.CustomUser'

# اللغة والوقت
LANGUAGE_CODE = 'ar'
TIME_ZONE = 'Asia/Riyadh'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('ar', _('العربية')),
    ('en', _('الإنجليزية')),
]

LOCALE_PATHS = [BASE_DIR / 'locale']

# إعدادات الملفات الثابتة
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# إعداد Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dwuqinjmj',
    'API_KEY': '873348181376647',
    'API_SECRET': 'J9w5pKFEMc5v1No61bmchMWG0v0',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

cloudinary.config(
    cloud_name='dwuqinmjg',
    api_key='615189195894851',
    api_secret='4yCAOOQfPQ4tMQNQ7hCma-7SKg0',
    secure=True
)

# نوع الحقول الافتراضي
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# إعدادات تسجيل الدخول والخروج
LOGIN_URL = '/accounts/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/accounts/login/'
