from django.conf.urls import patterns, include, url
from account import views

urlpatterns = patterns('',
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.user_logout, name='user_logout'),
)