"""
Django settings for projekt project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+o*uvw+#=+2v#b^w^d7fo-$#6fldngc0)8-t(p0)b@(n8&yqyw'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Moje aplikacje
    'portal',
    'nauczyciel',

    #Aplikacje innych firm
    'bootstrap3',
    'django_summernote',
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

ROOT_URLCONF = 'projekt.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'projekt.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

LOGIN_URL='/login'

#Ustawienia dla django-bootstrap3
BOOTSTRAP3 = {
    'include_jquery': True,
    }

#Ustawienia dla Summernote
SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode, default
    'iframe': True,

    # Or, you can set it as False to use SummernoteInplaceWidget by default - no iframe mode
    # In this case, you have to load Bootstrap/jQuery stuff by manually.
    # Use this when you're already using Bootstraip/jQuery based themes.
#    'iframe': False,

    # You can put custom Summernote settings
    'summernote': {
        # As an example, using Summernote Air-mode
#        'airMode': False,

        # Change editor size
        'width': '100%',
        'height': '480',

        # Use proper language setting automatically (default)
#        'lang': None,

        # Or, set editor language/locale forcely
        'lang': 'pl-PL',

        # You can also add custom settings for external plugins
#        'print': {
#            'stylesheetUrl': '/some_static_folder/printable.css',
#        },
    },

    # Need authentication while uploading attachments.
#    'attachment_require_authentication': True,

    # Set `upload_to` function for attachments.
#    'attachment_upload_to': my_custom_upload_to_func(),

    # Set custom storage class for attachments.
#    'attachment_storage_class': 'my.custom.storage.class.name',

    # Set custom model for attachments (default: 'django_summernote.Attachment')
#    'attachment_model': 'my.custom.attachment.model', # must inherit 'django_summernote.AbstractAttachment'

    # You can disable attachment feature.
#    'disable_attachment': False,

    # You can add custom css/js for SummernoteWidget.
#    'css': (
#    ),
#    'js': (
#    ),

    # You can also add custom css/js for SummernoteInplaceWidget.
    # !!! Be sure to put {{ form.media }} in template before initiate summernote.
#    'css_for_inplace': (
#    ),
#    'js_for_inplace': (
#    ),

    # Codemirror as codeview
    # If any codemirror settings are defined, it will include codemirror files automatically.
#    'css': {
#        '//cdnjs.cloudflare.com/ajax/libs/codemirror/5.29.0/theme/monokai.min.css',
#    },
#    'codemirror': {
#        'mode': 'htmlmixed',
#        'lineNumbers': 'true',
#
#        # You have to include theme file in 'css' or 'css_for_inplace' before using it.
#        'theme': 'monokai',
#    },

    # Lazy initialize
    # If you want to initialize summernote at the bottom of page, set this as True
#    # and call `initSummernote()` on your page.
#    'lazy': True,

    # To use external plugins,
    # Include them within `css` and `js`.
#    'js': {
#        '/some_static_folder/summernote-ext-print.js',
#        '//somewhere_in_internet/summernote-plugin-name.js',
#    },
}

#Ustawienia dla Heroku
if os.getcwd() == '/app':
    import dj_database_url
    DATABASES = {
        'default': dj_database_url.config(default='postgres://localhost/login')
    }

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    #Zezwolenie na nagłówki hosta
    ALLOWED_HOSTS = ['*']

    #Konfiguracja zasobów
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, 'staticfiles'))
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
)
