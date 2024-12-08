INSTALLED_APPS = [
    ...
    'blog',
]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
STATIC_URL = '/static/'

TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / "blog/templates"],
        ...
    },
]
INSTALLED_APPS += [
    'taggit',
]
