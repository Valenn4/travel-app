from .base import *

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

# SECURITY
CORS_ORIGIN_ALLOW_ALL = False
CORS_ORIGIN_WHITELIST = (
"http://valenn2.pythonanywhere.com",
)
#SECURE_SSL_REDIRECT = True
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'production.sqlite3',
    }
}