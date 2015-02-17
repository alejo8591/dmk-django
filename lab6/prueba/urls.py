from django.conf.urls import patterns, url
from prueba import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)