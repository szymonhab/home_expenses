import datetime

from django.shortcuts import render, redirect
from django.http import Http404, HttpResponseRedirect, JsonResponse
from django.core.urlresolvers import reverse
from django.core import serializers
from django.contrib.auth.decorators import permission_required
from django.db.models import Sum

from .models import Bill, Category, BillRow
from .forms import BillForm, SummaryDateForm
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
            bill = BillService.create_bill_from_form_data(form.cleaned_data)

            return HttpResponseRedirect(reverse('expenses_app:bill_details', args=[bill.id]))
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


@permission_required('expenses_app.access_workspace')
def charts(request):
    return render(request, 'expenses_app/charts/charts.html', {})


@permission_required('expenses_app.access_workspace')
def get_two_weeks_data():
    date_from = datetime.date.today() - datetime.timedelta(days=14)
    bills = Bill.objects.filter(bill_date__gt=date_from, bill_date__lt=datetime.date.today(), workspace=1).values(
        'bill_date').annotate(day_sum=Sum('amount'))

    two_weeks_data = {str(datetime.date.today() - datetime.timedelta(days=x)): 0 for x in range(0, 14)}
    for bill in bills:
        two_weeks_data[str(bill['bill_date'])] = str(bill['day_sum'])

    return JsonResponse(two_weeks_data, safe=False)


@permission_required('expenses_app.access_workspace')
def summary(request):
    date = datetime.date.today()
    if request.method == 'POST':
        form = SummaryDateForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
    else:
        form = SummaryDateForm()

    categories = Category.objects.filter(workspace=1)
    bills = Bill.objects.filter(bill_date__month=date.month, bill_date__year=date.year, workspace=1)
    summary_data = {}

    for category in categories:
        rows = BillRow.objects.filter(category=category, bill__in=list(bills)).aggregate(category_sum=Sum('amount'))
        summary_data[category.id] = {
            'category_name': category.name,
            'amount': rows['category_sum']
        }

    return render(request, 'expenses_app/summary/summary.html', {
        'date': date,
        'summary_data': summary_data,
        'bills_sum': bills.aggregate(bills_sum=Sum('amount'))['bills_sum'],
        'form': form
    })
