from django import forms

from .models import Person
from .models import Shop


class BillForm(forms.Form):
    person = forms.ModelChoiceField(queryset=Person.objects.all())
    shop = forms.ModelChoiceField(queryset=Shop.objects.all())
    amount = forms.DecimalField(max_digits=8, decimal_places=2)
    bill_date = forms.DateField()
    rows = forms.CharField(widget=forms.HiddenInput)
