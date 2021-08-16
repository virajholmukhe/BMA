from django.contrib import admin
from django.urls import path
from django.urls.conf import include, re_path

from . import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin_7507507535/', admin.site.urls),
    path('',include('UserApp.urls')),
    path('accounts/',include('UserApp.urls')),
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT})
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

