from .base import *

SECRET_KEY = 'django-insecure-s-%m@-*i9z*xlstvm+nyzeg3-i%74vfws-glk%u#5232%(j74!'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
