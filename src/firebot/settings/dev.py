import os
from firebot.settings.base import *  # noqa


###############################################################################
# Django
###############################################################################
DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SECRET_KEY = 'o*3#%*xmxb2dgfpn$1835f1p49!i=9kuq(e#zvczkcvg1d)xsk'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'mediafiles'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'firebot',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}


###############################################################################
# Celery
###############################################################################

CELERY_TASK_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True
# CELERY_BROKER_URL = 'redis://localhost:6379/1'
