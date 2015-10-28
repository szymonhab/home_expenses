from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bill/$', views.new_bill, name='new_bill'),
    url(r'^bill/(?P<bill_id>[0-9]+)/$', views.bill_details, name='bill_details'),
    url(r'^bill/(?P<bill_id>[0-9]+)/delete/$', views.delete_bill, name='delete_bill'),
    url(r'^bill/two_weeks_data/$', views.get_two_weeks_data, name='two_weeks_data'),
    url(r'^charts/$', views.charts, name='charts'),
    url(r'^summary/$', views.summary, name='summary'),
]
