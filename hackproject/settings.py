"""
Django settings for hackproject project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
#import dj_database_url
import os
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v1_($c12r32ds#wj+ug**j5vi&o5h9gt^0y&x#1y$5j(s!ay(3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#TEMPLATE_DEBUG=True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'social_django',
    'google_auth',

    'hackapp',
    'crispy_forms',

    'easy_maps',

    'star_ratings'


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
   # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware'
]

ROOT_URLCONF = 'hackproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS':[os.path.join(BASE_DIR,'templates')],
        #'DIRS':[os.path.join(SETTINGS_PATH,'templates')],
        'DIRS':['templates'],
        #'DIRS':[PROJECT_DIR.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

              #  'social_django.context_processors.backends'
                'social_django.context_processors.login_redirect',
                
              #  'django.core.context_processors.request'
            ],
        },
    },
]

WSGI_APPLICATION = 'hackproject.wsgi.application'

AUTHENTICATION_BACKENDS=(
    'social_core.backends.facebook.FacebookOAuth2',
  #  "google_auth.authentication.GoogleAuthBackend"

    'django.contrib.auth.backends.ModelBackend'
)
# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'ENGINE': 'django.db.backends.mysql',
        #'Name':'DB_NAME',
        #'USER':'DB_USER',
        #'PASSWORD':'DB_PASSWORD',
        #'HOST':'localhost',
        #'PORT':'3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'



#ACCOUNT_ACTIVATION_DAYS=7
EMAIL_HOST='localhost'
EMAIL_PORT=102
#EMAIL_HOST_USERNAME=''
#EMAIL_HOST_PASSWORD=''
EMAIL_USE_TLS=False
EMAIL_USE_SLS=False
#DEFAULT_FROM_EMAIL=''
#if DEBUG:
 #   STATIC_ROOT = "/django_projects/hack/hackproject/hackapp/static/sign.css"
STATICFILES_DIRS=(os.path.join(BASE_DIR,'static'),)


SOCIAL_AUTH_FACEBOOK_KEY="2471036739640671"
SOCIAL_AUTH_FACEBOOK_SECRET="8fde02560f1d8e1be9211b65819e1e56"



EASY_MAPS_GOOGLE_KEY='AIzaSyBAm_uUidKhRkRrOaFnMehhBykqIuP6iy0'


EASY_MAPS_CENTER = (-41.3, 32)


SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='762001228928-6utdihfagqfloij7bjvi4gj84mt76hc6.apps.googleusercontent.com'

SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET='jbL5VvvkYnGsdMKw09o8iIX9'