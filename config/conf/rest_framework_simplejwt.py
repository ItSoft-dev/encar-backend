from datetime import timedelta


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": True,
    'AUTH_COOKIE': 'jwt_token',  # JWT token saqlanadigan cookie nomi
    'AUTH_HEADER_TYPES': ('Bearer',),  # Token turi
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION', # Header nomi
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',
}