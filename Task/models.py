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
    assigned_to = models.IntegerField('Assigned_to',null=True)
    assign_date = models.DateField('assign date', help_text='task assignment day', blank=False, null=True)
    deadline = models.DateField('deadline', help_text='task deadline', blank=False, null=True)
    task_description=models.CharField('description',max_length=500,null=True)
    status = models.CharField(choices=STATUS_TYPE, max_length=25, default='In Progress')

    def __str__(self):
        return f'{self.task_title} {self.user}'
    def close_task(self):
        self.status="Completed"
        self.save()

