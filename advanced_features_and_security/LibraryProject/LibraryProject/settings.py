AUTH_USER_MODEL = 'accounts.CustomUser'
INSTALLED_APPS = [
    ...
    'accounts',
]
from django.conf import settings

class Librarian(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
