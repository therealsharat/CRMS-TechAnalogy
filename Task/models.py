from django.db import models
from Employee.models import Employee, Department
from django.contrib.auth.models import User

# Create your models here.

# ENUMS
STATUS_TYPE = (
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed'),
)

# TASK MODEL
class Task (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    task_title = models.CharField('Title', max_length=30, help_text="Heading for the task", blank=False, null=True)
    description = models.TextField('Description', max_length=255, help_text="Description for the task", blank=False, null=True)

    assign_date = models.DateField('assign date', help_text='task assignment day', blank=False, null=True)
    deadline = models.DateField('deadline', help_text='task deadline', blank=False, null=True)

    status = models.CharField(choices=STATUS_TYPE, max_length=25, default='In Progress')
    is_approved = models.BooleanField(default=False)
    department = models.CharField('department', max_length=30, default=None, null=True)

    def __str__(self):
        return f'{self.task_title} {self.user}'

# def get_user_list():
#     UserList = []
#     for i in User.objects.all():
#         UserList[i] = i.username
