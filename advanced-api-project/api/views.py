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
