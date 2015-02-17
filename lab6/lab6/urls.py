from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^prueba/', include('prueba.urls')),
    url(r'^testing/', include('testing.urls')),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'^uploads/(?P<path>.*)',
		'serve',
		{
			'document_root': settings.MEDIA_ROOT
		}),
	)
