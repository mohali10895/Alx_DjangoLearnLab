INSTALLED_APPS = [
    # Other apps...
    'rest_framework',
    'rest_framework.authtoken',
    'api',  # your app
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}
