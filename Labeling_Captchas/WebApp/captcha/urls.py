from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('login/', auth_views.login,name = 'login'),
    path('namer/', include('namer.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
