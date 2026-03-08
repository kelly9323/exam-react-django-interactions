from .base import *

SECRET_KEY = 'django-insecure-s-%m@-*i9z*xlstvm+nyzeg3-i%74vfws-glk%u#5232%(j74!'

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
