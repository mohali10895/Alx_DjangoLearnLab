from django.contrib import admin
from .models import Book

# Register the Book model with custom admin settings
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns to display in the list view
    list_filter = ('author', 'publication_year')  # Add filters for author and publication year
    search_fields = ('title', 'author')  # Allow searching by title and author
