from django import forms
from .models import *

class BookSearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)



class BookForm(forms.ModelForm):
    contributors = forms.ModelMultipleChoiceField(queryset=Contributor.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'contributors', 'isbn', 'publication_date']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
            'contributors': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }


class BookImageForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['image']


class ContributorForm(forms.ModelForm):
    class Meta:
        model = Contributor
        fields = ['first_names', 'last_names', 'email']