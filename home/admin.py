from django.contrib import admin
from .models import Book_Store,Author,Category
# Register your models here.

@admin.register(Book_Store)
class Book_Store_Admin(admin.ModelAdmin):
    list_display = ('pk', 'book_title', 'publication_date', 'category', 'author', 'price', 'description')

@admin.register(Author)
class Author_Admin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'address')

@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display = ('pk', 'name')
