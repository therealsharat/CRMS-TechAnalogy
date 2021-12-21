from django.urls import include, path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.Login, name='Login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Employee/Logout.html'), name='Logout'),
]