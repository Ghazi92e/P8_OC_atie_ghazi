from . import *

SECRET_KEY = '2i166t6u1$$unibb+bumybw0cy+o_9@d469i+b3n70#+e+_)cOg'
DEBUG = False
ALLOWED_HOSTS = ['161.35.214.115']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'products_purbeurre',
        'USER': 'ghazi',
        'PASSWORD': 'Liban',
        'HOST': '',
        'PORT': '5432',
    }
}

