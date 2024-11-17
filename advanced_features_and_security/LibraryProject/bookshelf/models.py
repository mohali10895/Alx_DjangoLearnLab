from django.db import models
from django.conf import settings  # For referencing the custom user model

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    genre = models.CharField(max_length=100, blank=True, null=True)
    copies_available = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    books = models.ManyToManyField(Book, related_name="libraries", blank=True)

    def __str__(self):
        return self.name


class Librarian(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="librarian_profile")
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="librarians")

    def __str__(self):
        return f"{self.user.username} - {self.library.name}"


class Member(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="member_profile")
    membership_date = models.DateField(auto_now_add=True)
    library = models.ForeignKey(Library, on_delete=models.CASCADE, related_name="members")

    def __str__(self):
        return self.user.username


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrows")
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="borrows")
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(blank=True, null=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book.title} borrowed by {self.member.user.username}"
