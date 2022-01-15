"""Billion_Dollar_Code URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from Employee import views as employee_views
from django.conf import settings
from django.conf.urls.static import static
from leave import views as leave_views
from Resignation import views as resig_views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Employee.urls')),
    path('leave_request/', leave_views.LeaveRequest, name='leave_request'),
    path('dashboard/', include('Dashboard.urls')),
    path('register/', employee_views.Register, name='register' ),
    path('leave_creation/', leave_views.leave_creation, name='leave_creation'),
    path('resignation/', resig_views.resignation, name='resignation')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
