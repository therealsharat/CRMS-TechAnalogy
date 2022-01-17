
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [


    path('Resignation_creation', views.resignation_creation, name='Resignation_creation'),
    path('Resignation_status',views.resignation_status,name='Resignation_status'),
    path('Resignation_request',views.resignation_request,name='Resignation_request'),
    path("file_download",views.FileDownload,name="file_download")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
