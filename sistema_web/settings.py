"""
Django settings for sistema_web project.
Generado por Django 5.2.7
"""

import os
from pathlib import Path

# ========================
# RUTAS BASE
# ========================
BASE_DIR = Path(__file__).resolve().parent.parent

# ========================
# SEGURIDAD
# ========================
SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-joiv@pfdl5!t3$gyr)6_8p_j9*9p&7in%s4t=bjozr4yl$q+yz')

# ⚠️ IMPORTANTE:
# En Render, define DEBUG=False como variable de entorno
DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'sistema-mercedario.onrender.com'
]

CSRF_TRUSTED_ORIGINS = ['https://sistema-mercedario.onrender.com']


# ========================
# APLICACIONES INSTALADAS
# ========================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'estudiantes',
    'usuarios',
]

# ========================
# MIDDLEWARE
# ========================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # ✅ Necesario para servir archivos estáticos en Render
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ========================
# URLS Y TEMPLATES
# ========================
ROOT_URLCONF = 'sistema_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'sistema_web.wsgi.application'

# ========================
# BASE DE DATOS
# ========================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ========================
# VALIDACIÓN DE CONTRASEÑAS
# ========================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ========================
# INTERNACIONALIZACIÓN
# ========================
LANGUAGE_CODE = 'es-es'   # Cambié a español
TIME_ZONE = 'America/Guayaquil'  # Ajusta según tu país
USE_I18N = True
USE_TZ = True

# ========================
# ARCHIVOS ESTÁTICOS
# ========================
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']   # carpeta local opcional
STATIC_ROOT = BASE_DIR / 'staticfiles'     # carpeta usada por Render

# Whitenoise permite servir archivos estáticos comprimidos en producción
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 🔐 Configuración de login/logout
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/registrar/'        # ✅ después de iniciar sesión
LOGOUT_REDIRECT_URL = '/login/'           # después de cerrar sesión

# ========================
# CLAVE PRIMARIA
# ========================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
