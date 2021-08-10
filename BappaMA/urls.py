from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('UserApp.urls')),
    path('accounts/',include('UserApp.urls')),
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)