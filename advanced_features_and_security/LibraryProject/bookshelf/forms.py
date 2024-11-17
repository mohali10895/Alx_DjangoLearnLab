# bookshelf/forms.py
from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=255, required=True, label="Book Title")
    author = forms.CharField(max_length=255, required=True, label="Author")
    published_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2025)), label="Published Date")
