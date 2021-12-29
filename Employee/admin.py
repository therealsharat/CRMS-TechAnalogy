from django.contrib import admin
from Employee.models import *

# Register your models here.

admin.site.register(Department)
admin.site.register(Role)
admin.site.register(Employee)
