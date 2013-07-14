"""For production use, uses mysql database.

"""

from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'djangocoffee',     # Or path to database file if using sqlite3.
        'USER': 'dailykm',                      # Not used with sqlite3.
        'PASSWORD': '2Sr3x99g',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
