from django.shortcuts import render
from .models import Book_Store,Author,Category
from .serializers import Book_Store_Serializers
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404


class Book_Store_List_Create_View(APIView):
    def get(self,request):
        book_store = Book_Store.objects.all().order_by('publication_date')
        serializer  = Book_Store_Serializers(book_store, many=True)
        return Response(serializer.data)

    def post(self,request):
        book_store_serializer = Book_Store_Serializers(data=request.data)
        if book_store_serializer.is_valid():
            book_store_serializer.save()
            return Response(book_store_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(book_store_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Update_Dalete_Book_Store(APIView):
    def get_object(self,pk):
        try:
            return Book_Store.objects.get(pk=pk)
        except Book_Store.DoesNotExist:
            raise Http404

    def get(self,request,pk):
        book_store = self.get_object(pk)
        serializer  = Book_Store_Serializers(book_store)
        return Response(serializer.data)

    def put(self,request,pk):
        book_store = self.get_object(pk)
        serializer = Book_Store_Serializers(book_store, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        book_store = self.get_object(pk)
        book_store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Search_by_name(APIView):
    def get(self,request,name):
        try:
            book_store=Book_Store.objects.filter(book_title__icontains=name)
        except Book_Store.DoesNotExist:
            raise Http404
        serializer  = Book_Store_Serializers(book_store,many=True)
        return Response(serializer.data)

class Get_List_Of_Books_grouped_by_category(APIView):
    def get(self,request,category_id):
        try:
            category = Category.objects.filter(pk=category_id).exists()
            if category:
                count_of_book= Book_Store.objects.filter(category=category_id).count()
            else:
                raise Http404
        except Book_Store.DoesNotExist:
            raise Http404
        return Response({"Get_List_Of_Books_grouped_by_category":count_of_book})
