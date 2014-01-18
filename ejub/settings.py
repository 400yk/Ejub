"""
Django settings for ejub project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# STATIC_ROOT = os.path.join(BASE_DIR, 'ej/static').replace('\\','/')
STATIC_ROOT = os.path.join(BASE_DIR, '../../ejub_static').replace('\\','/')

# SITE_ID: 3 is development, 2 is production
SITE_ID = 2

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v*089on$q#wm3h*f=m=yi8c-r3wa!gl-o8fvdo!&)^w42^_x=9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

TEMPLATE_CONTEXT_PROCESSORS = (
    # Required by allauth template tags
    "django.core.context_processors.request",
    'django.contrib.auth.context_processors.auth',

    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
    )

LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_QUERY_EMAIL = True
SOCIALACCOUNT_PROVIDERS = {
        'facebook': {
            'SCOPE': ['email', 'publish_stream'],
            'METHOD': 'js_sdk'
            }
        }

SOCIALACCOUNT_PROVIDERS['linkedin'] = {
            'SCOPE': ['r_emailaddress'],
            'PROFILE_FIELDS': ['id','first-name','last-name','email-address','picture-url','public-profile-url']}

AUTHENTICATION_BACKENDS = (
        # Needed to login by username in Django admin, regardless of 'allauth'
        "django.contrib.auth.backends.ModelBackend",

        # 'allauth' specific authentication methods, such as login by e-mail
        "allauth.account.auth_backends.AuthenticationBackend",
        )


# This is a production setting
ALLOWED_HOSTS = [
        '.ejub.us',
        '.ejub.us.',
        ]

if 'DJANGO_SETTINGS_MODULE' not in os.environ:
    os.environ['DJANGO_SETTINGS_MODULE'] = 'ejub.settings'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    'ej',

    # The Django sites framework is required
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.linkedin',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ejub.urls'

WSGI_APPLICATION = 'ejub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test_ej',
        'USER': 'youngwide',
        'PASSWORD': '198989',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = 'http://www.ejub.us/ej/static/'

try:
    from settings_dev import *
except ImportError, e:
    pass


