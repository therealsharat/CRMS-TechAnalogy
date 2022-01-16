from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from Employee.models import Department
from datetime import date
# Create your models here.

#enums
LEAVE_TYPE = (
('sick','Sick Leave'),
('casual','Casual Leave'),
('emergency','Emergency Leave'),
('study','Study Leave')
)
STATUS_TYPE = (
('Pending','Pending'),
('Approved','Approved'),
('Rejected','Rejected'),
)

class leave(models.Model):
    applied_date=models.DateField('applied_date',default=date.today)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    startdate = models.DateField('startdate', help_text='start data of employment', blank=False, null=True)
    enddate = models.DateField('enddate', help_text='end date of employment', blank=False, null=True)
    leavetype = models.CharField(choices=LEAVE_TYPE, max_length=25, default='sick', null=True, blank=False)
    reason = models.CharField('Reason', max_length=255, help_text='add additional information for leave', null=True, blank=True)
    status=models.CharField(choices=STATUS_TYPE, max_length=25,default='Pending')
    is_approved=models.BooleanField(default=False)
    department= models.CharField('department',max_length=30,default=None,null=True)

    def __str__(self):
        return ('{0} - {1}'.format(self.leavetype, self.user))

    def get_leave(self):
        leave=self.leavetype
        user=self.user
        employee=user.employee.get_name
        return ('{0}-{1}'.format(employee,leave))
    def approve_leave(self):
        if not self.is_approved:
            self.is_approved=True
            self.status='Approved'
            self.save()
    def reject_leave(self):
        self.is_approved=False
        self.status='Rejected'
        self.save()
