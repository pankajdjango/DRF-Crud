from rest_framework import serializers
from .models import Book_Store,Author,Category

class Author_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields  = "__all__"

class Category_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields  = "__all__"

class Book_Store_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Book_Store
        fields  = "__all__"
