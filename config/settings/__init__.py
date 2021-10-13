from .base import *
import os

ROOT_URLCONF = 'config.urls'

if os.environ['DJANGO_ENV'] == 'production'  :
    from .production import *
else : 
    from .development import *
