from django.conf.urls import patterns, include, url
from order import views

urlpatterns = patterns('',
    url(r'^$', views.order_index, name='order_index'),
    url(r'^detail/(?P<order_id>\d+)/$', views.order, name='order'),
    url(r'^add/$', views.add_order, name='add_order'),
    url(r'^edit/(?P<order_id>\d+)/$', views.order_edit, name='order_edit'),
    # URLs Customer
    url(r'^customer/$', views.customer_list, name='customer_list'),
    url(r'^customer/ajax/$', views.button_customer_list, name='button_customer_list'),
    url(r'^customer/detail/(?P<customer_slug>[\w\-]+)/$', views.customer, name='customer'),
    url(r'^customer/add/$', views.add_customer, name='add_customer'),
    url(r'^customer/edit/(?P<customer_id>\d+)/$', views.customer_edit, name='customer_edit'),
    # URLs Product
    url(r'^product/add/$', views.add_product, name='add_product'),
    url(r'^product/list/$', views.product_list, name='product_list'),
    url(r'^product/detail/(?P<product_id>\d+)/$', views.product, name='product'),
    url(r'^product/edit/(?P<product_id>\d+)/(?P<stock_id>\d+)/$', views.product_edit, name='product_edit'),
    url(r'^product/like/$', views.like_product, name='like_product'),
)