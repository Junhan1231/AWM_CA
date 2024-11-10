from pathlib import Path
import os
import socket

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-4bc=g6!mbw5+njyb69o6pc$l(w0k6@!tz99og8-s#)u6f*t80b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # 设置为 False 用于生产环境

# 替换为你的域名
ALLOWED_HOSTS = ['awmcaproject.info', 'localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'map',
    'crispy_forms',
    'leaflet',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'advanced_web_mapping_ca1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'advanced_web_mapping_ca1.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gis',
        'USER': 'docker',
        'PASSWORD': 'docker',
        'HOST': 'localhost' if socket.gethostname() == "JunhandeMacBook-Pro.local" else 'wmap-postgis',
        'PORT': '25432' if socket.gethostname() == "JunhandeMacBook-Pro.local" else '5432',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# 使用 whitenoise 管理静态文件以便于部署
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (53.0, -8.0),
    'DEFAULT_ZOOM': 6,
}

# 安全设置
if os.getenv('DEPLOY_SECURE') == 'True':
    DEBUG = False
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
else:
    DEBUG = True
    CSRF_COOKIE_SECURE = False
    SESSION_COOKIE_SECURE = False
