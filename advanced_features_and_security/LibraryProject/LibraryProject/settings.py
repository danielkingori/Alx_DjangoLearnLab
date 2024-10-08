"""
Django settings for LibraryProject project.

Generated by 'django-admin startproject' using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-vcpjw_jb1psq)@)7=2u$n_!_%sjuaej(aej_)r79bbev%jlmam'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'dan',
        'PASSWORD': 'tukcu123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
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

ROOT_URLCONF = 'LibraryProject.urls'

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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        'USER': 'dan',
        'PASSWORD': 'tukcu123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = "bookshelf.CustomUser"


#production env secure settings

# Enable the XSS Filter
# The SECURE_BROWSER_XSS_FILTER setting is used to enable the X-XSS-Protection header, which helps prevent reflected XSS attacks.
SECURE_BROWSER_XSS_FILTER = True

# Prevent Clickjacking
# The X_FRAME_OPTIONS setting is used to control whether your site can be embedded in an iframe.
# 'DENY' ensures that your pages cannot be displayed in an iframe.
# 'SAMEORIGIN' allows embedding only if the iframe is from the same origin.
X_FRAME_OPTIONS = 'DENY'  # or 'SAMEORIGIN'

# Prevent Content-Type Sniffing
# The SECURE_CONTENT_TYPE_NOSNIFF setting is used to enable the X-Content-Type-Options header, which prevents browsers from trying to guess the content type of a response.
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enforce HTTPS for CSRF cookies
CSRF_COOKIE_SECURE = True

# Enforce HTTPS for session cookies
SESSION_COOKIE_SECURE = True
# Set to True to redirect all non-HTTPS requests to HTTPS.
SECURE_SSL_REDIRECT = True
# Set an appropriate value, this case 1 year to instruct browsers to only access the site via HTTPS for the specified time.
SECURE_HSTS_SECONDS = 31536000
# to include all subdomains in the HSTS policy and to allow preloading.
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True
# to ensure session cookies are only transmitted over HTTPS.
SESSION_COOKIE_SECURE = True
# to ensure CSRF cookies are only transmitted over HTTPS.
CSRF_COOKIE_SECURE = True
# Set to “DENY” to prevent your site from being framed and protect against clickjacking.
X_FRAME_OPTIONS = 'DENY'
#  Set to True to prevent browsers from MIME-sniffing a response away from the declared content-type.
SECURE_CONTENT_TYPE_NOSNIFF = True
# Set to True to enable the browser’s XSS filtering and help prevent cross-site scripting attacks.
SECURE_BROWSER_XSS_FILTER = True
# Tells Django to trust the `HTTP_X_FORWARDED_PROTO` header sent by your reverse proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')