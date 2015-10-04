from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Bill
from .forms import BillForm


def index(request):
    latest_bill_list = Bill.objects.order_by('-add_datetime')[:10]
    context = {
        'latest_bill_list': latest_bill_list
    }

    return render(request, 'expenses_app/index.html', context)  # ("Test index, total bill amount: %0.2f" % bills_amount


def bill_details(request, bill_id):
    try:
        bill = Bill.objects.get(pk=bill_id)  # get_object_or_404(Question, pk=question_id)
    except Bill.DoesNotExist:
        raise Http404("Bill does not exist")

    return render(request, 'expenses_app/bill/details.html', {'bill': bill})


def new_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            person = form.cleaned_data['person']
            amount = form.cleaned_data['amount']
            bill_date = form.cleaned_data['bill_date']
            rows = form.cleaned_data['rows']
            shop = form.cleaned_data['shop']
            bill = Bill(bill_date=bill_date, amount=amount, person=person, workspace=1)
            bill.save()

            return HttpResponseRedirect(reverse('expenses_app:new_bill'))
    else:
        form = BillForm()

    return render(request, 'expenses_app/bill/new-bill.html', {'form': form})
