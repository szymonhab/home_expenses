from django.shortcuts import render
from django.http import Http404

from .models import Bill


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

    return render(request, 'expenses_app/bill/new-bill.html', {})
