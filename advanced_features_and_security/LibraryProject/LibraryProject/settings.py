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
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['yourdomain.com']  # Replace with your domain or server IP

# Security Settings
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Content Security Policy (CSP)
CSP_DEFAULT_SRC = ("'self'",)
CSP_SCRIPT_SRC = ("'self'", "'unsafe-inline'")  # Adjust as needed
CSP_STYLE_SRC = ("'self'", "'unsafe-inline'")  # Adjust as needed


# settings.py

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True

# Enable HTTP Strict Transport Security (HSTS) for one year (31536000 seconds)
SECURE_HSTS_SECONDS = 31536000

# Include subdomains in HSTS policy
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allow browsers to preload the HSTS policy
SECURE_HSTS_PRELOAD = True

