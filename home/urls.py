from django.urls import path
from . import views
urlpatterns = [
    path('book-store/',views.Book_Store_List_Create_View.as_view()),
    path('book-store-action/<int:pk>/',views.Update_Dalete_Book_Store.as_view()),
    path('book-store-search/<name>/',views.Search_by_name.as_view()),
    path('book-get-list-by-category/<int:category_id>/',views.Get_List_Of_Books_grouped_by_category.as_view()),
]
