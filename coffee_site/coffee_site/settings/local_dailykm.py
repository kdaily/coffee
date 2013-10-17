"""For local usage, kenny's version.

"""

from .base import *

DEBUG = True
TEMPLATE_DEBUG = True #DEBUG

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'djangocoffee',     # Or path to database file if using sqlite3.
#         'USER': 'dailykm',                      # Not used with sqlite3.
#         'PASSWORD': '2Sr3x99g',                  # Not used with sqlite3.
#         'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
#         'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'djangocoffee',     # Or path to database file if using sqlite3.
        'USER': 'coffeesite',                      # Not used with sqlite3.
        'PASSWORD': '1234',                  # Not used with sqlite3.
        'HOST': '192.168.1.4',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # default
    'guardian.backends.ObjectPermissionBackend',
)

# For django-guardian
ANONYMOUS_USER_ID = -1

