"""
    Generated by 'django-admin startproject' using Django 3.2.9.
"""

import os
from pathlib import Path
from decouple import config 








#############################################################
#############################################################
#############################################################
#######                                             #########
#######                                             #########
#######                  ROOT CONFIGS               #########
#######                                             #########
#######                                             #########
#############################################################
#############################################################
#############################################################
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
INTERNAL_IPS = ['127.0.0.1']
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
WSGI_APPLICATION = 'ivoire_api.wsgi.application'
ROOT_URLCONF = 'ivoire_api.urls'
ADMINS = [
    ('Claver DIBY', 'claverdiby9@gmail.com'),
    ('stefanci.com Support', 'support@stefanci.com'),
    ('Claver DIBY | stefanci.com', 'claverdiby@stefanci.com')
]





SITE_NAME = 'IVOIRE APIs' # Name to be displayed in templates
ADMIN_PAGE_URL = 'admin' # Admin page URL
PROJECT_DB_MODE = 'sqlite' # For detecting db type & credentials (production, sqlite)






# List of URLs from where we are scraping articles' contents.
NEWS_SCRAPING_URLS = [
    ('Ivoire Hebdo', 'https://ivoirhebdo.com/'),
    ('Abidjan.net', 'https://news.abidjan.net/'),
    ('Jeune Afrique', 'https://www.jeuneafrique.com/'), #pays/cote-divoire/
    ('Linfodrome', 'https://www.linfodrome.com/'),
    ('AIP - Agence Ivoirienne de Presse', 'https://www.aip.ci/'),
    ('Fraternité matin', 'https://www.fratmat.info/'),
]




RECIPES_SCRAPING_URLS = []



#############################################################
#############################################################
#############################################################
#######                                             #########
#######                                             #########
#######       INSTALLED APPLICATIONS DEFINITION     #########
#######                                             #########
#######                                             #########
#############################################################
#############################################################
#############################################################
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',



    # 3rd PARTY APPS
    'storages',
    'ckeditor',
    'corsheaders',
    'import_export',
    'rest_framework',
    # 'drf_api_logger',
    'cloudinary_storage',



    # LOCALE APPS
    'core.apps.CoreConfig',
    'news.apps.NewsConfig',
    'receipes.apps.ReceipesConfig',
]











#############################################################
#############################################################
#############################################################
#######                                             #########
#######                                             #########
#######             MIDDLEWARES                     #########
#######                                             #########
#######                                             #########
#############################################################
#############################################################
#############################################################
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Added
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # Added
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'drf_api_logger.middleware.api_logger_middleware.APILoggerMiddleware',  # Added
]







#############################################################
#############################################################
#############################################################
#######                                             #########
#######                                             #########
#######                 TEMPLATES                   #########
#######                                             #########
#######                                             #########
#############################################################
#############################################################
#############################################################
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'ivoire_api.context_processors.site' #Added
            ],
        },
    },
]








#############################################################
#############################################################
#############################################################
#######                                             #########
#######                                             #########
#######               DATABASES                     #########
#######                                             #########
#######                                             #########
#############################################################
#############################################################
#############################################################

DATABASES = {
    'default': {
        'ENGINE': config('DEFAULT_DB_ENGINE'),
        'NAME': config('DEFAULT_DB_NAME'),
    },
}












#############################################################
#############################################################
#############################################################
#######                                             #########
#######                                             #########
#######             PASSWORD VALIDATORS             #########
#######                                             #########
#######                                             #########
#############################################################
#############################################################
#############################################################
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







#############################################################
#############################################################
#############################################################
#######                                             #########
#######                                             #########
#######             INTERNATIONALIZATION            #########
#######                                             #########
#######                                             #########
#############################################################
#############################################################
#############################################################
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True












#############################################################
#############################################################
#############################################################
#######                                             #########
#######                                             #########
#######          STATIC & MEDIA FILES CONFIGS       #########
#######                                             #########
#######                                             #########
#############################################################
#############################################################
#############################################################
STATIC_URL = '/files/'
STATIC_ROOT = 'collectstatic/files/'

MEDIA_URL = 'ivoire/files/uploads/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'files/')]
MEDIA_ROOT = os.path.join(BASE_DIR, 'files/ivoire/uploads')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME'),
    'API_KEY' : config('CLOUDINARY_API_KEY'),
    'API_SECRET' : config('CLOUDINARY_API_SECRET'),
}

if DEBUG == False:
    DEFAULT_FILE_STORAGE = config('DEFAULT_CLOUDINARY_FILE_STORAGE')










#############################################################
#############################################################
#############################################################
#######                                             #########
#######                                             #########
#######                  EMAIL CONFIGS              #########
#######                                             #########
#######                                             #########
#############################################################
#############################################################
#############################################################
if PROJECT_DB_MODE == 'production':
    EMAIL_BACKEND = config('EMAIL_BACKEND')
    EMAIL_HOST = config('EMAIL_HOST')
    EMAIL_PORT = config('EMAIL_PORT', cast=int)
    EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
    EMAIL_HOST_USER = config('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
    EMAIL_USE_LOCALTIME = config('EMAIL_USE_LOCALTIME', cast=bool)

if PROJECT_DB_MODE != 'production':
    EMAIL_BACKEND = config('CONSOLE_EMAIL_BACKEND')











#############################################################
#############################################################
#############################################################
#######                                             #########
#######                                             #########
#######           3rd PARTY APPS CONFIGS            #########
#######                                             #########
#######                                             #########
#############################################################
#############################################################
#############################################################








#############################################################
#############################################################
########             CKEDITOR CONFIGS            ############
#############################################################
#############################################################
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'extraPlugins': ','.join(
            [
                'codesnippet',
            ]
        ),
        'codeSnippet_theme': 'monokai_sublime',
    },
}
CKEDITOR_UPLOAD_PATH = os.path.join(BASE_DIR, 'files/ivoire_api/uploads/editors/')
CKEDITOR_BROWSE_SHOW_DIRS = True








#############################################################
#############################################################
########            CORS HEADERS CONFIGS          ###########
#############################################################
#############################################################
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = []










#############################################################
#############################################################
########            REST FRAMEWORK CONFIGS        ###########
#############################################################
#############################################################
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}






#############################################################
#############################################################
########              API LOGGER CONFIGS          ###########
#############################################################
#############################################################
# DRF_API_LOGGER_DATABASE = True
# DRF_API_LOGGER_SIGNAL = True
# DRF_LOGGER_QUEUE_MAX_SIZE = 1
# DRF_LOGGER_INTERVAL = 1
# DRF_API_LOGGER_EXCLUDE_KEYS = []



