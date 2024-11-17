AUTH_USER_MODEL = 'accounts.CustomUser'
AUTH_USER_MODEL = 'bookshelf.CustomUser'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',  # Custom user app
    'bookshelf',  # App for book and library models
]

from django.conf import settings

class Librarian(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
