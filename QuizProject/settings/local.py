from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '../db.sqlite3', # This is where you put the name of the db file.
                 # If one doesn't exist, it will be created at migration time.
    }
}