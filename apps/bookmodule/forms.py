from django import forms
from .models import Book , Student, Student2 , Address, Address2 , ImageModel

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'quantity', 'pubdate', 'rating', 'publisher', 'authors']
        widgets = {
            'pubdate': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']


class ImageModelForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['title', 'description', 'image']