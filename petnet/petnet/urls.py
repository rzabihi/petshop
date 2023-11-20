from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from azbankgateways.urls import az_bank_gateways_urls

from core.views import frontpage, about, go_to_gateway_view, callback_gateway_view

admin.autodiscover()

# app_name = 'core'

urlpatterns = [
    path('about/', about, name='about'),
    path('admin/', admin.site.urls),
    path('bankgateways/', az_bank_gateways_urls()),
    path('go-to-gateway/', go_to_gateway_view),
    path('callback-gateway/', callback_gateway_view),
    path('', include('userprofile.urls')),
    path('', include('store.urls')),
    path('', frontpage, name='frontpage'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
