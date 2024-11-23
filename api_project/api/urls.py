from django.urls import path
from .views import BookList

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
]

from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookList, BookViewSet

# Initialize the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

# Define URL patterns
urlpatterns = [
    # Existing route for BookList
    path('books/', BookList.as_view(), name='book-list'),

    # Include the router's URLs
    path('', include(router.urls)),
]

from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('', include(router.urls)),
]


from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path

urlpatterns = [
    # Other routes...
    path('auth/token/', obtain_auth_token, name='api-token-auth'),
]
