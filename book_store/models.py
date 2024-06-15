from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    publication_date = models.DateField()
    image_url = models.URLField(max_length=255, blank=True, null=True)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

class BookAuthor(models.Model):
    image_url = models.URLField(max_length=255, blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)