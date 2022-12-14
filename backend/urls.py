from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('product.urls')),
    path("accounts/email/", page_not_found,{'exception': Exception('Not Found')}, name="account_email"),
    path('chaining/', include('smart_selects.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)