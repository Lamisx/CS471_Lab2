from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
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
path('simple/query', views.simple_query, name='books.simple_query'),
path('complex/query', views.complex_query, name='books.complex_query'),
path('lab8/task1', views.lab8_task1, name='lab8_task1'),
path('lab8/task2', views.lab8_task2, name='lab8_task2'),
path('lab8/task3', views.lab8_task3, name='lab8_task3'),
path('lab8/task4', views.lab8_task4, name='lab8_task4'),
path('lab8/task5', views.lab8_task5, name='lab8_task5'),
path('lab8/task7', views.lab8_task7, name='lab8_task7'),
path('lab9/task1/', views.lab9_task1, name='lab9_task1'),
path('lab9/task2/', views.lab9_task2, name='lab9_task2'),
path('lab9/task3/', views.lab9_task3, name='lab9_task3'),
path('lab9/task4/', views.lab9_task4, name='lab9_task4'),
path('lab9/task5/', views.lab9_task5, name='lab9_task5'),
path('lab9/task6/', views.lab9_task6, name='lab9_task6'),
path('lab10_part1/listbooks', views.list_books, name='listbooks'),
path('lab10_part1/addbook', views.add_book, name='add_book'),
path('lab10_part1/editbook/<int:id>', views.edit_book, name='edit_book'),
path('lab10_part1/deletebook/<int:id>', views.delete_book, name='delete_book'),
path('lab10_part2/addbook', views.add_book_form, name='add_book_form'),
path('lab10_part2/editbook/<int:id>', views.edit_book_form, name='edit_book_form'),
path('lab11/liststudents', views.list_students, name='list_students'),
path('lab11/addstudent', views.add_student, name='add_student'),
path('lab11/updatestudent/<int:id>', views.update_student, name='update_student'),
path('lab11/deletestudent/<int:id>', views.delete_student, name='delete_student'),
path('lab11/liststudents2', views.list_students2, name='list_students2'),
path('lab11/addstudent2', views.add_student2, name='add_student2'),
path('lab11/updatestudent2/<int:id>', views.update_student2, name='update_student2'),
path('lab11/deletestudent2/<int:id>', views.delete_student2, name='delete_student2'),
path('lab11/upload_image', views.upload_image, name='upload_image'),
path('lab11/list_images', views.list_images, name='list_images'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

