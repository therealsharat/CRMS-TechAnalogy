from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

#enums
LEAVE_TYPE = (
('sick','Sick Leave'),
('casual','Casual Leave'),
('emergency','Emergency Leave'),
('study','Study Leave')
)

class leave(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    startdate = models.DateField('startdate', help_text='start data of employment', blank=False, null=True)
    enddate = models.DateField('enddate', help_text='end date of employment', blank=False, null=True)
    leavetype = models.CharField(choices=LEAVE_TYPE, max_length=25, default='sick', null=True, blank=False)
    reason = models.CharField('Reason', max_length=255, help_text='add additional information for leave', null=True, blank=True)
    def __str__(self):
        return ('{0} - {1}'.format(self.leavetype, self.user))