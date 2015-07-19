"""
Django settings for cms project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import platform

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(PROJECT_PATH, '..'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i2d+e6$y419ydlof9k4&&f=zqyfm29zbefonar13t%=a_k-rhy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django_medusa',
    'cms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'cms.search',
    # debug tool bar 
    'django.contrib.staticfiles',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware' ,
)
  
ROOT_URLCONF = 'cms.urls'

WSGI_APPLICATION = 'cms.wsgi.application'

TIMEOUT=None

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'cms.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://127.0.0.1:8000/media/'

USE_I18N = True

USE_L10N = True

USE_TZ = True
TIME_ZONE = 'EST'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

SITE_ID = 1

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_ROOT, 'templates/' 'cms/'),
    os.path.join(PROJECT_ROOT, 'templates/'),
)

# django_medusa -- disk-based renderer
import os
MEDUSA_RENDERER_CLASS = "django_medusa.renderers.DiskStaticSiteRenderer"
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
MEDUSA_DEPLOY_DIR = os.path.join(
    PROJECT_DIR, '..', "_output"
)

DELICIOUS_USER='yowang'
DELICIOUS_PASSWORD='onNHHxe7aBkfG2t1LnGb'

ADMINS = (
    ('Hugh Wang', 'yowang@verizon.net'),
)

MANAGERS = ADMINS

AKISMET_API_KEY = '580527a0990b'

EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend' 
EMAIL_HOST = 'smtp.gmail.com'  
EMAIL_PORT = '465'
DEFAULT_FROM_EMAIL = 'changeme@gmail.com'
EMAIL_HOST_USER = 'changeme@gmail.com'
EMAIL_HOST_PASSWORD = 'changemexx'
#EMAIL_USE_TLS = True




# GOT "local_settings.py" ?
try:
    from local_settings import *
except ImportError:
    pass

