# clubinferno/settings/dev.py
# -*- coding: UTF-8 -*-
from .base import *
import os

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'house-inventory',
        'USER': 'admin',
        'PASSWORD': 'house-inventory',
        'HOST': 'postgres',
        'PORT': '5432'
    }
}
