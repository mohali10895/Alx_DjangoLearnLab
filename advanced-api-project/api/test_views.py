from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author
from rest_framework.reverse import reverse

class BookAPITestCase(APITestCase):

    def setUp(self):
        """Set up initial data for tests."""
        self.author = Author.objects.create(name="J.K. Rowling")
        self.book = Book.objects.create(
            title="Harry Potter and the Philosopher's Stone",
            publication_year=1997,
            author=self.author
        )
        self.user = User.objects.create_user(username='testuser', password='password')
        self.url = reverse('book-list')  # Assuming 'book-list' is the URL name for the list view

    def test_create_book(self):
        """Test creating a new book."""
        data = {
            'title': 'Harry Potter and the Chamber of Secrets',
            'publication_year': 1998,
            'author': self.author.id
        }
        self.client.login(username='testuser', password='password')
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """Test updating an existing book."""
        data = {'title': 'Harry Potter and the Goblet of Fire'}
        self.client.login(username='testuser', password='password')
        response = self.client.put(reverse('book-detail', kwargs={'pk': self.book.id}), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Harry Potter and the Goblet of Fire')

    def test_delete_book(self):
        """Test deleting a book."""
        self.client.login(username='testuser', password='password')
        response = self.client.delete(reverse('book-detail', kwargs={'pk': self.book.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_by_author(self):
        """Test filtering books by author."""
        author2 = Author.objects.create(name="George R.R. Martin")
        Book.objects.create(title="A Game of Thrones", publication_year=1996, author=author2)
        response = self.client.get(self.url, {'author': self.author.id}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.author.id)

    def test_search_books_by_title(self):
        """Test searching books by title."""
        response = self.client.get(self.url, {'search': 'Harry Potter'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_order_books_by_publication_year(self):
        """Test ordering books by publication year."""
        Book.objects.create(title="Harry Potter and the Prisoner of Azkaban", publication_year=1999, author=self.author)
        response = self.client.get(self.url, {'ordering': 'publication_year'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Harry Potter and the Philosopher\'s Stone')

    def test_permissions_for_unauthenticated_user(self):
        """Test that unauthenticated users can only GET data."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response = self.client.post(self.url, {'title': 'New Book', 'publication_year': 2024, 'author': self.author.id})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
