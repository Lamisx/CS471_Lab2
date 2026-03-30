from django.urls import path
from . import views
urlpatterns = [
 path('index2/<int:val1>/', views.index2),
 path('', views.index, name= "books.index"),
 path('list_books/', views.list_books, name= "books.list_books"),
 path('aboutus/', views.aboutus, name="books.aboutus"),
 path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
path('html5/links/', views.links, name='links'),
path('text/formatting/', views.formatting, name='formatting'),
path('html5/listing/', views.listing, name='listing'),
path('html5/tables/', views.tables, name='tables'),
path('search/', views.search, name='books.search'),
]

