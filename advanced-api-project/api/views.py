from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookListView(mixins.ListModelMixin, generics.GenericAPIView):
    """Retrieve all books."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class BookCreateView(mixins.CreateModelMixin, generics.GenericAPIView):
    """Create a new book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    """Retrieve a single book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class BookUpdateView(mixins.UpdateModelMixin, generics.GenericAPIView):
    """Update an existing book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class BookDeleteView(mixins.DestroyModelMixin, generics.GenericAPIView):
    """Delete a book."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# Import the required modules
from django_filters.rest_framework import DjangoFilterBackend  # For filtering functionality
from rest_framework import filters, generics  # For search, ordering, and generic views
from rest_framework.permissions import IsAuthenticatedOrReadOnly  # For permission handling
from .models import Book  # Import the Book model
from django_filters import rest_framework
from rest_framework import generics

from .serializers import BookSerializer  # Import the BookSerializer

class BookListView(generics.ListCreateAPIView):
    """List all books or create a new book."""
    queryset = Book.objects.all()  # Queryset for retrieving all books
    serializer_class = BookSerializer  # Serializer used to convert Book objects to JSON
    permission_classes = [IsAuthenticatedOrReadOnly]  # Set permission classes
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)  # Enable filtering, searching, and ordering
    filterset_fields = ['title', 'author', 'publication_year']  # Fields that can be filtered
    search_fields = ['title', 'author']  # Fields that can be searched
    ordering_fields = ['title', 'publication_year']  # Fields that can be ordered by
    ordering = ['title']  # Default ordering by title


