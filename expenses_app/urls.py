from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bill/$', views.new_bill, name='new_bill'),
    url(r'^bill/(?P<bill_id>[0-9]+)/$', views.bill_details, name='bill_details'),
]
