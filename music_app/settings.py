"""
Django settings for music_app project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
import yaml

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# Load credentials file
with open(os.path.join(BASE_DIR, 'credentials.yaml'), 'r') as file:
    credentials = yaml.safe_load(file)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = credentials['DJANGO_SECRET_KEY']

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
    'rest_framework',
    'api.apps.ApiConfig',
    'frontend.apps.FrontendConfig',
    'spotify.apps.SpotifyConfig',
    'rest_framework.authtoken',
    'django_crontab',
    'django_extensions',
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

ROOT_URLCONF = 'music_app.urls'

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

WSGI_APPLICATION = 'music_app.wsgi.application'

# Cron jobs
CRONJOBS = [
    ('0 0 * * *', 'spotify.cron.get_data'),
    #('50 * * * *', 'spotify.cron.say_hello')
]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
db_username = credentials['MONGODB_USERNAME']
db_password = credentials['MONGODB_PASSWORD']
db_cluster = credentials['MONGODB_CLUSTER']
db_database = credentials['MONGODB_DATABASE']
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'djongo',
        'NAME': 'spotifyDataDB',
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': f'mongodb+srv://{db_username}:{db_password}@{db_cluster}/{db_database}?retryWrites=true&w=majority'
        }
    }
}

SESSION_COOKIE_AGE = 60*60*24*30

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'spotify.User'

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

# Rest of config
SPOTIFY_CLIENT_ID = credentials['SPOTIFY_CLIENT_ID']
SPOTIFY_CLIENT_SECRET = credentials['SPOTIFY_CLIENT_SECRET']

TELEGRAM_BOT_TOKEN = credentials['TELEGRAM_BOT_TOKEN']
TELEGRAM_BOT_CHAT_ID = credentials['TELEGRAM_BOT_CHAT_ID']


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
