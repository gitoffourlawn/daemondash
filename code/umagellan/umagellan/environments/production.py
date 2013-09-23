import os

DEBUG = False
TEMPLATE_DEBUG = False
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

SITE_ROOT = 'umagellan/' 

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'umagellan',                      # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'apache',
        'PASSWORD': 'umagellan2013',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}
