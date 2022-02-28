import os

from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test2',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

REDIS_SERVER = '127.0.0.1'  # 数据库IP或域名
CACHES = {
    # 缓存view数据
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://" + REDIS_SERVER + ":6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "PASSWORD": "",  # 数据库密码
        }
    },
}
