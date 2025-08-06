REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],

    # 'DEFAULT_PAGINATION_CLASS': 'core.apps.shared.paginations.custom.CustomPageNumberPagination',
    # 'PAGE_SIZE': 10,
    # 'DEFAULT_THROTTLE_CLASSES': [
    #     'rest_framework.throttling.AnonRateThrottle',
    #     'rest_framework.throttling.UserRateThrottle',
    # ],
    # 'DEFAULT_THROTTLE_RATES': {
    #     'anon': '100/minute',  
    #     'user': '100/minute',
    # },
}