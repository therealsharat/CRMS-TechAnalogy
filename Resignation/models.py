from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.utils import timezone
STATUS_TYPE = (
('Pending','Pending'),
('Approved','Approved'),
('Rejected','Rejected'),
)
# Create your models here.
class Resignation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    applied_date=models.DateField(default=timezone.now)
    Termination_date=models.DateField()
    reason=models.CharField(max_length=150)
    is_approved=models.BooleanField(default=False)
    status=models.CharField(choices=STATUS_TYPE,max_length=25,default='Pending')

    def __str__ (self):
        return ('{0}'.format(self.user))
    def Approve(self):
        if not self.is_approved:
            self.is_approved=True
            self.status='Approved'
            self.save()
    def Reject(self):
        self. is_approved=False
        self.status='Rejected'
        self.save()