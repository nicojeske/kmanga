"""
Django settings for kmanga project.

Generated by 'django-admin startproject' using Django 2.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '18k7lr2so(vnb*y8&yr1b0tf-bcygm7#(%%#inx8fm4pskro1$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = 'kmanga.urls'

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

WSGI_APPLICATION = 'kmanga.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'


# KManga specific configuration

INSTALLED_APPS += [
    # External applications
    'django_rq',
    'easy_thumbnails',
    # Project applications
    'core.apps.CoreConfig',
    'proxy.apps.ProxyConfig',
    'registration.apps.RegistrationConfig',
    'scrapyctl.apps.ScrapyCtlConfig',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

THUMBNAIL_ALIASES = {
    '': {
        'cover': {
            'size': (270, 360),
            'crop': 'smart',
            'upscale': True,
            'bw': True,
        },
    },
}

RQ_QUEUES = {
    'default': {
        'HOST': 'db',
        'PORT': 6379,
        'DB': 0,
    },
    'high': {
        'HOST': 'db',
        'PORT': 6379,
        'DB': 0,
    },
    'low': {
        'HOST': 'db',
        'PORT': 6379,
        'DB': 0,
    }
}

KINDLEGEN = os.path.join(BASE_DIR, '..', 'bin', 'kindlegen')
# IMAGES_STORE and ISSUES_STORE are also in `scraper` settings
IMAGES_STORE = os.path.join(BASE_DIR, '..', 'scraper', 'img_store')
ISSUES_STORE = os.path.join(BASE_DIR, '..', 'scraper', 'issue_store')
MOBI_STORE = os.path.join(BASE_DIR, '..', 'scraper', 'mobi_store')
VOLUME_MAX_SIZE = 12 * 1024**2

SCRAPY_SETTINGS_MODULE = 'scraper.settings'
SCRAPY_ACCOUNTS = {}

DEFAULT_FROM_EMAIL = 'admin@kmanga.net'

CONTACT_EMAIL = 'admin@kmanga.net'

KMANGA_EMAIL = 'kindle@kmanga.net'

# Import local settings
try:
    from .local_settings import *
except ImportError:
    pass