INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',  # For token authentication
    'accounts',
    'posts',
]
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'yourapp.herokuapp.com', 'localhost']
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True  # Redirect all HTTP requests to HTTPS
DATABASES = {
    'default': dj_database_url.config(default='postgres://USER:PASSWORD@HOST:PORT/NAME')
}
