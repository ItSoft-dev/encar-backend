from config.env import env

CACHES = {
    "default": {
        "BACKEND": 'django_redis.cache.RedisCache',
        "LOCATION": env.str('REDIS_URL', 'redis://127.0.0.1:6379'),
        "TIMEOUT": 5,
    },
}

CACHE_MIDDLEWARE_SECONDS = 5


CACHEOPS_REDIS = env.str('REDIS_URL','redis://127.0.0.1:6379')
CACHEOPS_DEFAULTS = {
    "timeout": 5,
}

CACHEOPS = {
    "accounts.*": {
        "ops": "all", 
        "timeout": 60 * 5,
    },
}
CACHEOPS_DEGRADE_ON_FAILURE = True
CACHEOPS_ENABLED = False