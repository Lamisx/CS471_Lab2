from datetime import datetime
from .forms import BookForm, ImageModelForm, Student2, Student2Form , StudentForm
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Book, ImageModel , Student, Address , Publisher, Author
from django.db.models import Q 
from django.db.models import Count, Sum, Avg, Max, Min 

def index(request):
 name = request.GET.get("name") or "world!"
 return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1 = 0): 
 return HttpResponse("value1 = "+str(val1))
def viewbook(request, bookId):
 # assume that we have the following books somewhere (e.g. database)
 book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
 book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
 targetBook = None
 if book1['id'] == bookId: targetBook = book1
 if book2['id'] == bookId: targetBook = book2
 context = {'book':targetBook} # book is the variable name accessible by the template
 return render(request, 'bookmodule/show.html', context)

def index(request):
 return render(request, "bookmodule/index.html")
"""def list_books(request):
 return render(request, 'bookmodule/list_books.html')"""
def viewbook(request, bookId):
 return render(request, 'bookmodule/one_book.html')
def aboutus(request):
 return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/books/html5/links.html')
def formatting(request):
    return render(request, 'bookmodule/books/text/formatting.html')
def listing(request):
    return render(request, 'bookmodule/books/html5/listing.html')
def tables(request):
    return render(request, 'bookmodule/books/html5/tables.html')

def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]


def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower().strip()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True

            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

   
    return render(request, 'bookmodule/search.html')
#-------------------LAB7------------------
def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')
#-------------------LAB8------------------
def lab8_task1(request):
    mybooks = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': mybooks})
def lab8_task2(request):
    mybooks = Book.objects.filter(Q(edition__gt=3) & (Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/lab8_task2.html', {'books': mybooks})
def lab8_task3(request):
    mybooks = Book.objects.filter(~Q(edition__gt=3) & ~(Q(title__icontains='qu') | Q(author__icontains='qu')))
    return render(request, 'bookmodule/lab8_task3.html', {'books': mybooks})
def lab8_task4(request):
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': mybooks})
def lab8_task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})

def lab8_task7(request):
    city_stats = Address.objects.annotate(student_count=Count('student'))
    return render(request, 'bookmodule/lab8_task7.html', {'city_stats': city_stats})

#-------------------LAB9------------------
def lab9_task1(request):
    books = Book.objects.all()

    total_quantity = Book.objects.aggregate(total=Sum('quantity'))['total'] or 0

    for book in books:
        if total_quantity > 0:
            book.availability_percentage = round((book.quantity / total_quantity) * 100, 2)
        else:
            book.availability_percentage = 0

    return render(request, 'bookmodule/lab9_task1.html', {'books': books})
def lab9_task2(request):
    publishers = Publisher.objects.annotate(total_stock=Sum('book__quantity'))
    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})
def lab9_task3(request):
    publishers = Publisher.objects.annotate(oldest_book_date=Min('book__pubdate'))    
    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})
def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('book__price'),
        min_price=Min('book__price'),
        max_price=Max('book__price')
    )
    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})
def lab9_task5(request):
    publishers = Publisher.objects.annotate(high_rated_count=Count('book', filter=Q(book__rating__gte=4)))
    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})
from django.db.models import Count, Q
# ...

def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        filtered_books_count=Count('book', filter=Q(
            book__price__gt=50, 
            book__quantity__lt=5, 
            book__quantity__gte=1
        ))
    )
    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})

#-------------------LAB10-1------------------
def list_books(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10/listbooks.html', {'books': books})

def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        publisher_id = request.POST.get('publisher')
        authors_ids = request.POST.getlist('authors')
        pubdate = request.POST.get('pubdate')
        rating = request.POST.get('rating')

        publisher = Publisher.objects.get(id=publisher_id)
        pubdate = datetime.fromisoformat(pubdate)

        book = Book.objects.create(
            title=title,
            price=price,
            quantity=quantity,
            publisher=publisher,
            pubdate=pubdate,
            rating=rating
        )

        book.authors.set(authors_ids)
        return redirect('listbooks')

    publishers = Publisher.objects.all()
    authors = Author.objects.all()
    return render(request, 'bookmodule/lab10/add_book.html', {
        'publishers': publishers,
        'authors': authors
    })

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.price = request.POST.get('price')
        book.quantity = request.POST.get('quantity')
        book.rating = request.POST.get('rating')
        pubdate_str = request.POST.get('pubdate')
        if pubdate_str:
            book.pubdate = datetime.fromisoformat(pubdate_str)

        publisher_id = request.POST.get('publisher')
        book.publisher = Publisher.objects.get(id=publisher_id)
        book.save()

        authors_ids = request.POST.getlist('authors')
        book.authors.set(authors_ids)
        return redirect('listbooks')

    publishers = Publisher.objects.all()
    authors = Author.objects.all()
    return render(request, 'bookmodule/lab10/edit_book.html', {
        'book': book,
        'publishers': publishers,
        'authors': authors
    })
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('listbooks')
#-------------------LAB10-2------------------
def add_book_form(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listbooks')
    else:
        form = BookForm()
    return render(request, 'bookmodule/lab10/book_form.html', {'form': form})
def edit_book_form(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('listbooks')
    else:
        form = BookForm(instance=book)
    return render(request, 'bookmodule/lab10/book_form.html', {'form': form})
#-------------------LAB11-------------------
def list_students(request):
    students = Student.objects.all()
    return render(request, 'bookmodule/lab11/list_students.html', {'students': students})
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm()
    return render(request, 'bookmodule/lab11/form.html', {'form': form})
def update_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'bookmodule/lab11/form.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('list_students')


def list_students2(request):
    students = Student2.objects.all()
    return render(request, 'bookmodule/lab11/list_students2.html', {'students': students})
def add_student2(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form()
    return render(request, 'bookmodule/lab11/form.html', {'form': form})
def update_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_students2')
    else:
        form = Student2Form(instance=student)
    return render(request, 'bookmodule/lab11/form.html', {'form': form})
def delete_student2(request, id):
    student = get_object_or_404(Student2, id=id)
    student.delete()
    return redirect('list_students2')


def upload_image(request):
    if request.method == 'POST':
        form = ImageModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_images')
    else:
        form = ImageModelForm()
    return render(request, 'bookmodule/lab11/upload_image.html', {'form': form})
def list_images(request):
    images = ImageModel.objects.all()
    return render(request, 'bookmodule/lab11/list_images.html', {'images': images})