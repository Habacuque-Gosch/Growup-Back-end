from pathlib import Path
import os
from corsheaders.defaults import default_headers
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = str(os.getenv('SECRET_KEY'))


DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',
                'localhost',
                'appelearning.onrender.com',
                ]

AUTH_USER_MODEL = 'users.CustomUser'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'apps.courses',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'setup.urls'

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

WSGI_APPLICATION = 'setup.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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


LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'setup/static')
# ]

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS_ORIGINS_ALLOW_aLL = True

CORS_ALLOW_ORIGINS = [
    'http://127.0.0.1:8000',
    'https://appelearning.onrender.com',
    'http://localhost:5173'
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'contenttype',
]

# CORS_ALLOW_HEADERS = "*"

CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:8000',
    'http://localhost:5173',
    'https://appelearning.onrender.com'
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.AllowAny'
        # 'rest_framework.permissions.IsAuthenticated'
        'rest_framework.permissions.IsAuthenticatedOrReadOnly'
        # 'rest_framework.permissions.IsAdminUser'
        # 'rest_framework.permissions.DjangoModelPermissions'

    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50
}

# LOGIN_REDIRECT_URL = '/'
# lOGOUT_REDIRECT_URL = '/'


# PAYMENT KEYS
# STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY', 'nullkey')
# STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', 'nullkey')
# STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET', 'nullkey')


# SECURITY/GPO and PROD
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
if ENVIRONMENT == 'production':
    print('**######### PROD #########**')
    SECRET_KEY = str(os.getenv('SECRET_KEY'))
    DEBUG = False

    # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    # EMAIL_HOST = 'smtp.gmail.com'
    # EMAIL_USE_TLS = True
    # EMAIL_PORT = 587
    # EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    # EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

    # SESSION_COOKIE_SECURE = True
    # CSRF_COOKIE_SECURE = True
    # SECURE_BROWSER_XSS_FILTER = True
    # SECURE_CONTENT_TYPE_NOSNIFF = True
    # SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    # SECURE_HSTS_SECONDS = 31536000
    # SECURE_REDIRECT_EXEMPT = []
    # SECURE_SSL_REDIRECT = True
    # SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")
    # SECURE_CONTENT_TYPE_NOSNIFF = True
    # SECURE_HSTS_PRELOAD = True
    # X_FRAME_OPTIONS = 'SAMEORING'
    # CSP_DEFAULT_SRC = ("'self'", "https://polyfill.io")
    # CSP_STYLE_SRC = ("'unsafe-inline'", "https:")