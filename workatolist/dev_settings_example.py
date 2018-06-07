"""
Development settings
"""

from .settings import INSTALLED_APPS


INSTALLED_APPS += (
    # APPS
)


# ALLOWED_HOSTS = ['*']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<db_name>',
        'USER': '<user>',
        'PASSWORD': '<password>',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
