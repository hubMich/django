from django import forms
from books.models import Author


class AuthorForm(forms.Form):
    pass

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        exclude = ()