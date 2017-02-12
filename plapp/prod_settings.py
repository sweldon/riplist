#Production settings
from plapp.base_settings import  *

DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.34.60.164']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'earthworks',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}

