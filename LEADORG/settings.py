from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables from .env file
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

# M-Pesa API Config from .env
MPESA_CONSUMER_KEY = os.getenv('MPESA_CONSUMER_KEY')
MPESA_CONSUMER_SECRET = os.getenv('MPESA_CONSUMER_SECRET')
MPESA_PASSKEY = os.getenv('MPESA_PASSKEY')
MPESA_SHORTCODE = os.getenv('MPESA_SHORTCODE')
MPESA_ENV = os.getenv('MPESA_ENV', 'sandbox')  # default to sandbox
MPESA_CALLBACK_URL = os.getenv('MPESA_CALLBACK_URL')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SECRET_KEY = 'django-insecure-fndni7(z2mx+3bbgk=v3h5rkq#v90b7)n2d-x%-9ex_%@k*bi)'



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp',
    'django_bootstrap5',
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

ROOT_URLCONF = 'LEADORG.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LEADORG.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # Make sure BASE_DIR is defined
] if os.path.exists(os.path.join(BASE_DIR, "static")) else []


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'mainapp.CustomUser'


AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'publicpages.authentication.EmailBackend',  # Custom email authentication
    'django.contrib.auth.backends.ModelBackend',  # Default Django authentication
]

SESSION_ENGINE = "django.contrib.sessions.backends.db"  # Uses the database
SESSION_COOKIE_AGE = 1209600  # 2 weeks (matches your logic)
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # Keep session alive even after closing the browser

# Redirect users to the homepage or dashboard after login
LOGIN_URL = '/login/' 
LOGIN_REDIRECT_URL = '/home/'
LOGOUT_REDIRECT_URL = '/home/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/home/'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "ramspheldonyango@gmail.com"
EMAIL_HOST_PASSWORD = "qakp qgtr inpn sapv"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


PAYPAL_CLIENT_ID = "ATkLED_rdrWQKqEWQteX4mV1CDpTgeJpKOHcFTsDO0D5sVOHEE5I8NvQP3CEBGoX-xYe-gXoAzjatjn3"
PAYPAL_CLIENT_SECRET = "ENNnPpE3bP_dyt9QzAqvM6cAttMsLTB7uJS01-OcBJhFqOtceVRIxp1DI2SlzL0-WYSjqN16QKgZv8_k"
PAYPAL_MODE = "sandbox"  # Change to "live" for real payments