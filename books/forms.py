from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class meta:
        model = Book
        fields = [
            "title",
            "description",
            "release-date",
            "read-counter",
        ]
