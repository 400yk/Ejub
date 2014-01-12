DEBUG = True
TEMPLATE_DEBUG = True

COMPRESS_AUTO = True
SESSTION_COOKIE_SECURE = True

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'test_ej',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': 'localhost',
            'PORT': '3306',
            }
        }

