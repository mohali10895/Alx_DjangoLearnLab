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


from rest_framework.viewsets.ModelViewSet import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    """
    A ViewSet for performing CRUD operations on the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
