from django.urls import path
from . import views


urlpatterns = [
    path('', views.Dashboard, name='Dashboard'),
    path('personal', views.Personal, name='Personal'),
    path('leave', views.Leave, name='Leave'),
    path('task_view', views.Task_View, name='Task View'),
    path('resignation',views.resignation, name='resignation'),
    path('task', views.Task, name='Task'),
]