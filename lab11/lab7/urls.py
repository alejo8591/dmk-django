from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from order.views import CustomerViewSet, ProductViewSet, StockViewSet, OrderViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'customer', CustomerViewSet)
router.register(r'product', ProductViewSet)
router.register(r'stock', StockViewSet)
router.register(r'order', OrderViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lab7.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^app/', include('app.urls')),
    url(r'^order/', include('order.urls')),
    url(r'^account/', include('account.urls')),

    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/' include('rest_framework.urls', namespace='rest_framework')),
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