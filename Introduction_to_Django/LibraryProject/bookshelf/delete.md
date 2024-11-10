### Delete Operation

Command:
```python
from bookshelf.models import Book  # Import the Book model

book = Book.objects.get(title="Nineteen Eighty-Four")  # Retrieve the book
book.delete()  # Delete the book
print(Book.objects.all())  # Verify the book has been deleted
