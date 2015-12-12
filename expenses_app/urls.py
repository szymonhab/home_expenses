from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bill/$', views.new_bill, name='new_bill'),
    url(r'^bill/(?P<bill_id>[0-9]+)/$', views.bill_details, name='bill_details'),
    url(r'^bill/(?P<bill_id>[0-9]+)/delete/$', views.delete_bill, name='delete_bill'),
    url(r'^bill/two-weeks-data/$', views.get_two_weeks_data, name='two_weeks_data'),
    url(r'^bill/show-all/(?P<page>[0-9]+)/$', views.bill_show_all, name='bill_show_all'),
    url(r'^bill/show-all/$', views.bill_show_all, name='bill_show_all'),
    url(r'^charts/$', views.charts, name='charts'),
    url(r'^summary/$', views.summary, name='summary'),
]
