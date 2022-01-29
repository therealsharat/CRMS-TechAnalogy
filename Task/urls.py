from django.urls import include, path
from Task import views as task_views
urlpatterns = [
    path('task_creation/', task_views.task_creation, name='task_creation'),
    path('task_status/', task_views.task_status, name='task_status'),
    path('task_submission/', task_views.task_submission, name='task_submission'),
    path('task_assigned/', task_views.task_assigned, name='task_assigned'),

]
