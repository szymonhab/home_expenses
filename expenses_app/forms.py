import datetime

from django import forms

from .models import Person, Shop


class BillForm(forms.Form):
    person = forms.ModelChoiceField(queryset=Person.objects.filter(workspace=1))
    shop = forms.ModelChoiceField(queryset=Shop.objects.filter(workspace=1))
    amount = forms.DecimalField(max_digits=8, decimal_places=2, widget=forms.TextInput(
        attrs={
            'data-ng-model': 'bill.sum',
            'data-ng-pattern': 'sumPattern',
            'data-replacecomma': '',
            'data-ng-required': 'true'
        }))
    bill_date = forms.DateField()
    rows = forms.CharField(widget=forms.HiddenInput(
        attrs={'value': '{[{ bill.billRows|json }]}'}))


class SummaryDateForm(forms.Form):
    dateAttrs = {
        'placeholder': 'MM/YYYY',
        'data-ng-model': 'date',
        'data-ng-pattern': 'datePattern',
        'data-ng-required': 'true'
    }
    dateWidget = forms.DateInput(format='%m/%Y', attrs=dateAttrs)

    date = forms.DateField(initial=datetime.date.today(), input_formats=['%m/%Y'], widget=dateWidget)
    person = forms.ModelChoiceField(queryset=Person.objects.filter(workspace=1), required=False)
