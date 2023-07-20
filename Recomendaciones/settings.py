"""
Django settings for Proyecto_peliculas project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
from re import T

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-uj*hcm^yfe#75-z70*06_(_fuu=a_1h8utuue!pd^z!-c!b-=u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin', # custom panel admin
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'App_peliculas', # nuestra app de críticas
    'crispy_forms', # forms django con bootstrap

]

CRISPY_TEMPLATE_PACK = 'bootstrap4' # forms django con bootstrap

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Recomendaciones.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "App_peliculas/templates/"], # enlazo los templates de la app. Lo hice para poder extender algunos html de admin y poder customizarlos
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

WSGI_APPLICATION = 'Recomendaciones.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es' # 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, 'static')
    BASE_DIR / "static"
]

# MEDIA_ROOT = os.path.join(BASE_DIR, 'images')
MEDIA_ROOT = BASE_DIR / "static/images/"

MEDIA_URL = '/images/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Jazzmin customization
JAZZMIN_SETTINGS = {
    "site_title": "Recomendaciones",
    "site_header": "Recomendaciones",
    "site_logo": "images/iconos/claqueta(32x32).png",
    "welcome_sign":  "Bienvenido, iniciar secion", # Loggin
    
    #############
    # Side Menu #
    #############
    "site_brand": "Home", 
    "order_with_respect_to": ["App_peliculas", "App_peliculas.Pelicula", "App_peliculas.Director", "App_peliculas.Actor", "App_peliculas.Critica", "auth", "auth.user"],
    "icons": { # los iconos los saca de bootstrap "https://www.w3schools.com/icons/icons_reference.asp"
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "App_peliculas.Actor": "fas fa-user-ninja",
        "App_peliculas.Director": "fas fa-user-secret",
        "App_peliculas.Pelicula": "fas fa-film",
        "App_peliculas.Critica": "fab fa-rocketchat",
    },

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "vertical_tabs",

    # Menu de personalización dentro de la página admin
   "show_ui_builder": True,

    # agregar nuestro propio css
    "custom_css": "css/admin.css",
}

JAZZMIN_UI_TWEAKS = {
    # general
    "theme": "darkly",
    "dark_mode_theme": "darkly",
    # Side Menu
    "brand_colour": "navbar-blue",
    "sidebar": "sidebar-dark-blue",
    "sidebar_nav_flat_style": True,
    
    # Top Menu
    "navbar_small_text": True,
    "navbar": "navbar-dark",
    "navbar_fixed": False,
    
    # Body
    "body_small_text": True,
    "accent": "accent-blue",

    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
        "success": "btn-success",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
