"""
Django settings for covid_19 project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import configparser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

APP_NAME = 'covid_19'
SITE_ID = 40

ETC_DIR = '/etc/'

LOGIN_REDIRECT_URL = 'home_url'

INDEX_PAGE = 'covid-19.bhp.org.bw:8000'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '6s!hjo60ck5l6&0+zjzduh3$2zusju8llbif!q+y0gsh4v$$j%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
LIVE_SYSTEM = True

ALLOWED_HOSTS = [
    'localhost', 'covid-19.bhp.org.bw', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_crypto_fields.apps.AppConfig',
    'django_extensions',
    'edc_model_admin.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'covid19_register.apps.AppConfig',
    'covid_19.apps.EdcBaseAppConfig',
    'covid_19.apps.AppConfig'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
]

ROOT_URLCONF = 'covid_19.urls'

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

WSGI_APPLICATION = 'covid_19.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

mysql_config = configparser.ConfigParser()
mysql_config.read(os.path.join(ETC_DIR, APP_NAME, 'mysql.ini'))

# HOST = mysql_config['mysql']['host']
# DB_USER = mysql_config['mysql']['user']
# DB_PASSWORD = mysql_config['mysql']['password']
# DB_NAME = mysql_config['mysql']['database']
# PORT = mysql_config['mysql']['port']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

# dashboards
DASHBOARD_URL_NAMES = {
    'visitor_listboard_url': 'covid19_register:visitor_listboard_url',
    'employee_listboard_url': 'covid19_register:employee_listboard_url',
}

LAB_DASHBOARD_URL_NAMES = {}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'covid19_register/base.html',
    'visitor_listboard_template': 'covid19_register/listboard.html',
    'employee_listboard_template': 'covid19_register/listboard.html',
}

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Gaborone'

USE_I18N = True

USE_L10N = False

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'