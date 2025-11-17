from .settings import *

DEBUG = True

SECRET_KEY = 'dd5-ssfugf*2gu4jf-qv_!sooc3_tpycryse+yp8-31iu2$%7d'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'medic-search-admin',
        'USER': 'root',
        'PASSWORD': 'root'
    }
}

ALLOWED_HOSTS = ['127.0.0.1']
