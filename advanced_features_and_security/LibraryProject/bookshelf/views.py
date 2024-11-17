from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import UpdateView, CreateView
from .models import Book

# Function-based views
@permission_required('app_name.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'books/view_books.html', {'books': books})

@permission_required('app_name.can_create', raise_exception=True)
def create_book(request):
    # Logic for creating a book
    return render(request, 'books/create_book.html')

# Class-based views
class BookUpdateView(PermissionRequiredMixin, UpdateView):
    model = Book
    fields = ['title', 'author', 'published_date']
    template_name = 'books/edit_book.html'from django.contrib.auth.decorators import permission_required


from django.shortcuts import render
from .models import Book

@permission_required('app_name.can_view', raise_exception=True)
def book_list(request):
    """
    View to list all books. Requires 'can_view' permission.
    """
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

    permission_required = 'app_name.can_edit'








# bookshelf/views.py
from django.shortcuts import render
from .forms import ExampleForm  # Import the ExampleForm class

def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            published_date = form.cleaned_data['published_date']
            # For example, you might save the data to the database
            # Book.objects.create(title=title, author=author, published_date=published_date)
            # Or perform other actions with the data
            return render(request, 'bookshelf/form_example.html', {'form': form, 'message': 'Book successfully added!'})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})

