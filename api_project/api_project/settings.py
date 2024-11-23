INSTALLED_APPS = [
    # Default Django apps...
    'rest_framework',  # Add this
]
INSTALLED_APPS = [
    # Other apps...
    'api',  # Add this
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
