from django.conf.urls import patterns, include, url
from order import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<order_id>\d+)/$', views.order, name='order'),
    url(r'^customer/detail/(?P<customer_id>\d+)/$', views.customer, name='customer'),
)