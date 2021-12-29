from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# ENUMS

Gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)

Title = (
    ('Mr', 'Mr'),
    ('Mrs', 'Mrs'),
    ('Mss', 'Mss'),
)

Employment_Type = (
    ('Full-Time', 'Full-Time'),
    ('Part-Time', 'Part-Time'),
    ('Contract', 'Contract'),
    ('Intern', 'Intern'),
)


# HELPER CLASSES

class Department(models.Model):
    department_name = models.CharField(max_length=125, blank=True)
    description = models.CharField(max_length=125, null=True, blank=True)


class Role(models.Model):
    role_name = models.CharField(max_length=125, blank=True)
    description = models.CharField(max_length=125, null=True, blank=True)


# EMPLOYEE MODEL

class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(choices=Title, max_length=3, null=False, blank=False)
    gender = models.CharField(choices=Gender, max_length=6, null=False, blank=False)
    firstname = models.CharField('Firstname', max_length=125, null=False, blank=False)
    lastname = models.CharField('Lastname', max_length=125, null=False, blank=False)

    department = models.ManyToManyField(Department, verbose_name='Department')
    role = models.ManyToManyField(Role, verbose_name='Role')

    startdate = models.DateField('Employment Date', help_text='date of employment', blank=False, null=True)
    employeetype = models.CharField(choices=Employment_Type, max_length=15, blank=False, null=True)
    employeeid = models.CharField('Employee ID Number', max_length=10, null=True, blank=True)

    created = models.DateTimeField(verbose_name='Created', auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=True, null=True)
