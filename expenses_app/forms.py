from django import forms

from .models import Person, Shop


class BillForm(forms.Form):
    person = forms.ModelChoiceField(queryset=Person.objects.all())
    shop = forms.ModelChoiceField(queryset=Shop.objects.all())
    amount = forms.DecimalField(max_digits=8, decimal_places=2, widget=forms.TextInput(
        attrs={'data-ng-model': 'bill.sum', 'data-ng-pattern': 'sumPattern', 'data-replacecomma': ''}))
    bill_date = forms.DateField()
    rows = forms.CharField(widget=forms.HiddenInput(
        attrs={'value': '{[{ bill.billRows|json }]}'}))
