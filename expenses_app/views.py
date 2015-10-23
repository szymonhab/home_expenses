from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core import serializers
from django.contrib.auth.decorators import permission_required

from .models import Bill, Category
from .forms import BillForm
from .services import BillService


@permission_required('expenses_app.access_workspace')
def index(request):
    latest_bill_list = Bill.objects.order_by('-add_datetime')[:10]
    context = {
        'latest_bill_list': latest_bill_list
    }

    return render(request, 'expenses_app/index.html', context)  # ("Test index, total bill amount: %0.2f" % bills_amount


@permission_required('expenses_app.access_workspace')
def bill_details(request, bill_id):
    try:
        bill = Bill.objects.get(pk=bill_id)  # get_object_or_404(Question, pk=question_id)
    except Bill.DoesNotExist:
        raise Http404("Bill does not exist")

    return render(request, 'expenses_app/bill/details.html', {'bill': bill})


@permission_required('expenses_app.access_workspace')
def new_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            BillService.create_bill_from_form_data(form.cleaned_data)

            return HttpResponseRedirect(reverse('expenses_app:new_bill'))
    else:
        form = BillForm()

    categories = serializers.serialize('json', Category.objects.filter(workspace=1), fields='name')
    context = {
        'form': form,
        'categoriesJSON': categories.replace('"', "'"),
        'post': request.POST
    }

    return render(request, 'expenses_app/bill/new-bill.html', context)

@permission_required('expenses_app.access_workspace')
def delete_bill(request, bill_id):
    if request.method == 'POST':
        bill = Bill.objects.get(pk=bill_id)
        bill.delete()

    return redirect('expenses_app:index')
