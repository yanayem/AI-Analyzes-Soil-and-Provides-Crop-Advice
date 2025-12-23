
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-284n^dwcj7we)ny7ucj&@=qnz#olyw*g8e+e)(__!g_h46^fu!'

DEBUG = True

ALLOWED_HOSTS = []

ALLOWED_HOSTS = []
ALLOWED_HOSTS = ["soilmonitor.onrender.com", "localhost", "127.0.0.1"]

CSRF_TRUSTED_ORIGINS = [
    "https://soilmonitor.onrender.com",
    "http://localhost",
    "http://127.0.0.1"
]
TIME_ZONE = 'Asia/Dhaka' 
USE_TZ = True




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'soilcore',
    'soildata', 
    'weather',
    'chatApp'


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"  

ROOT_URLCONF = 'soilcore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'soilcore.wsgi.application'



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

#------------
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
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'staticfile'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [BASE_DIR, "static"]



CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    }
}


# -------------------------
# Login URLs (used by @login_required)
# -------------------------
LOGIN_URL = '/accounts/login/'  # Default login page
LOGIN_REDIRECT_URL = '/soildata/dashboard/'  # Redirect after login

# -------------------------
# Weather API Settings
# -------------------------
OPENWEATHER_API_KEY = "963804a07802e5371e2a2bd19f6a7afb"
WEATHER_CACHE_SECONDS = 900  # 15 min cache

# -------------------------
# Google Custom Search API Settings
# -------------------------


SEARCH_ENGINE_ID = "d4f67ec45810c4c76"

# -------------------------
# Chat / OpenAI / Gemini
# -------------------------
GEMINI_API_KEY = "AIzaSyAtdLvDmDGkLiQTf0WET-rpRxnOTFEPUQk"
CHAT_HISTORY_LIMIT = 50