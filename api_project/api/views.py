from rest_framework.generics import generics.ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializer

class BookViewSet(ModelViewSet):
    """
    A ViewSet for performing CRUD operations on the Book model.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
