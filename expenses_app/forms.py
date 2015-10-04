from django import forms


class BillForm(forms.Form):
    person = forms.ChoiceField()
    shop = forms.ChoiceField()
    amount = forms.DecimalField(max_digits=8, decimal_places=2)
    bill_date = forms.DateField()
    rows = forms.CharField(widget=forms.HiddenInput)
