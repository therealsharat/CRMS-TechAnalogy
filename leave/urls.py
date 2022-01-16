from django.contrib import admin
from django.urls import include, path
from Employee import views as employee_views
from django.conf import settings
from django.conf.urls.static import static
from leave import views as leave_views
from Resignation import views as resig_views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('leave_request/', leave_views.LeaveRequest, name='leave_request'),
    path('leave_creation/', leave_views.leave_creation, name='leave_creation'),
    path('leave_status/', leave_views.leave_status, name='leave_status'),

]
