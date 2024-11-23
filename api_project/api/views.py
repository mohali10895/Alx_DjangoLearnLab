from rest_framework.generics import generics.ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView

class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
