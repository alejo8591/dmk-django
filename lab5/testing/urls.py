from django.conf.urls import patterns, url
from testing import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^one/', views.one, name='one'),
	url(r'^two/', views.two, name='two'),
	url(r'^three/', views.three, name='three'),
)