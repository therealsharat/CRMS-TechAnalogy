from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

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

    def __str__(self):
        return f'{self.department_name} Department'


class Role(models.Model):
    role_name = models.CharField(max_length=125, blank=True)
    description = models.CharField(max_length=125, null=True, blank=True)

    def __str__(self):
        return f'{self.role_name}'

# EMPLOYEE MODEL

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(choices=Title, max_length=3, null=False, blank=False)
    gender = models.CharField(choices=Gender, max_length=6, null=False, blank=False)
    firstname = models.CharField('Firstname', max_length=125, null=False, blank=False)
    lastname = models.CharField('Lastname', max_length=125, null=False, blank=False)

    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    department = models.ManyToManyField(Department, verbose_name='Department')
    role = models.ManyToManyField(Role, verbose_name='Role')

    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True, default='0123456789')
    email = models.EmailField(max_length=124, default='abc@gmail.com')

    startdate = models.DateField('Employment Date', help_text='date of employment', blank=False, null=True)
    employeetype = models.CharField(choices=Employment_Type, max_length=15, blank=False, null=True)
    employeeid = models.CharField('Employee ID Number', max_length=10, null=True, blank=True)

    created = models.DateTimeField(verbose_name='Created', auto_now_add=True, null=True)
    updated = models.DateTimeField(verbose_name='Updated', auto_now=True, null=True)

    def get_role(self):
        r=''
        for role in self.role.all():
            r=r+role.role_name
        return r
    def get_department(self):
        r=''
        for department in self.department.all():
            r=r+department.department_name
        return r
    def get_name(self):
        first_name=self.firstname
        last_name=self.lastname
        if not first_name:
            return last_name
        elif not last_name:
            return first_name
        else:
            full_name=first_name+' '+last_name
            return full_name


    def __str__(self):
        return f'{self.user} Profile'
