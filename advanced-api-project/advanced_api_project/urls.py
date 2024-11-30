from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),  # List and Create
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),  # Retrieve
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]
