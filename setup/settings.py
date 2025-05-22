from pathlib import Path
import os
from corsheaders.defaults import default_headers
import sentry_sdk
from dotenv import load_dotenv
load_dotenv()

sentry_sdk.init(
    dsn=os.getenv('DJANGO_APP_SENTRY_DSN'),
    send_default_pii=True,
    environment='Development',
    release=str(os.getenv('DJANGO_APP_NAME', 'Growup')) + ' - ' + str(os.getenv('DJANGO_APP_VERSION', 'v1.0')),
    traces_sample_rate= 1.0,
)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-sadksakdoplsa;321321fdfds///////////dpsa;p******'

DEBUG = os.getenv('ENVIRONMENT', 'development')

ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS').split(', ')

SITE_ID = 2

# Application definition
INSTALLED_APPS = [
    'apps.users.apps.UsersConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',
    
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',

    'apps.destinations.apps.DestinationsConfig',

    # 'django.contrib.sites',
    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',
]

# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         'SCOPE': {
#             'profile',
#             'email'
#         },
#         'AUTH_PARAMS': {'access_type': 'online'}
#     }
# }

# INTERNAL_IPS = [
#     "",
# ]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'setup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'setup.context_processors.my_notifications'
            ],
        },
    },
]

WSGI_APPLICATION = 'setup.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

print('########### DB CONNECTED ###########')
# SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_CACHE_ALIAS = "default"

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": f"{str(os.getenv('LOCATION_REDIS'))}",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
# print('########### DB CACHE CONNECTED ###########')

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

# i18n
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('pt-br', 'Português (Brasil)'),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'None')
# CELERY_TIMEZONE = 'America/Sao_Paulo'
# CELERY_RESULT_BACKEND = ''

# DATA_UPLOAD_MAX_MEMORY_SIZE = 7242880

# STATIC FILES (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'setup/static')
]

# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# MEDIA_PATH
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

# S3 Amanzon
# INSTALLED_APPS += ['storages']
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = 'nome-do-seu-bucket'
# AWS_S3_REGION_NAME = 'us-east-1'
# AWS_QUERYSTRING_AUTH = False  # para URLs públicas
# # URL de mídia (ajustado automaticamente pelo storage)
# MEDIA_URL = f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.CustomUser'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'apps.users.models.EmailAuthBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',
)


# CORS_ORIGINS_ALLOW_aLL = True
CORS_ALLOW_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:5173'
]

CORS_ALLOW_HEADERS = list(default_headers) + [
    'contenttype',
]

# CORS_ALLOW_HEADERS = "*"
CORS_ORIGIN_WHITELIST = [
    'http://127.0.0.1:8000',
    'http://localhost:5173',
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
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50,

    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'anon': '10/min',
        'user': '50/min'
    },
}

# LOGIN_REDIRECT_URL = '/'
# lOGOUT_REDIRECT_URL = '/'

# PAYMENT KEYS
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY', 'nullkey')
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY', 'nullkey')
STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET', 'nullkey')

# GPO and Security
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
if ENVIRONMENT == 'production':
    print('############### PROD ###############')

    # see https://docs.sentry.io/platforms/python/data-management/data-collected/   
    sentry_sdk.init(
        dsn=os.getenv('DJANGO_APP_SENTRY_DSN'),
        send_default_pii=True,
        environment=os.getenv('ENVIRONMENT'),
        release=str(os.getenv('DJANGO_APP_NAME', 'Growup - REST API PROD')) + ' - ' + str(os.getenv('DJANGO_APP_VERSION', 'v1.0')),
        traces_sample_rate= 0.2,
    )

    SECRET_KEY = str(os.getenv('SECRET_KEY'))
    DEBUG = False
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_SECONDS = 31536000
    # SECURE_REDIRECT_EXEMPT = []
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")
    # SECURE_CONTENT_TYPE_NOSNIFF = True
    # SECURE_HSTS_PRELOAD = True
    X_FRAME_OPTIONS = 'SAMEORING'
    # CSP_DEFAULT_SRC = ("'self'", "https://polyfill.io")
    # CSP_STYLE_SRC = ("'unsafe-inline'", "https:")

