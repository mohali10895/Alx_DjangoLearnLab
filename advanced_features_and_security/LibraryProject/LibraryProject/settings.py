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

# settings.py

# Ensure session cookies are only sent over HTTPS
SESSION_COOKIE_SECURE = True

# Ensure CSRF cookies are only sent over HTTPS
CSRF_COOKIE_SECURE = True


# settings.py

# Prevent the site from being framed (protect against clickjacking)
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from MIME-sniffing a response away from the declared content-type
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable the browser's XSS filtering to prevent cross-site scripting attacks
SECURE_BROWSER_XSS_FILTER = True

SECURE_SSL_REDIRECT = True  # Redirect all HTTP to HTTPS
SECURE_HSTS_SECONDS = 31536000  # One year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Apply to subdomains
SECURE_HSTS_PRELOAD = True  # Enable HSTS preload
SECURE_BROWSER_XSS_FILTER = True  # Enable browser's XSS filter
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME sniffing
X_FRAME_OPTIONS = 'DENY'  # Prevent framing (clickjacking)
CSRF_COOKIE_SECURE = True  # Ensure CSRF cookies are secure (only sent over HTTPS)
SESSION_COOKIE_SECURE = True  # Ensure session cookies are secure (only sent over HTTPS)

# CSRF settings
CSRF_TRUSTED_ORIGINS = ['https://yourdomain.com', 'https://www.yourdomain.com']

# Add the following settings for reverse proxy (e.g., Nginx or Apache)
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
