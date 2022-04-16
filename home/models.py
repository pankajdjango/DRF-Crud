from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Book_Store(models.Model):
    book_title = models.CharField(max_length=50)
    publication_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
