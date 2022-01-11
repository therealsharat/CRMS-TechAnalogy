from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


# Create your models here.
class Resignation(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    Termination_date=models.DateField()
    reason=models.CharField(max_length=150)
    attachment=models.FileField(upload_to='resignation')
    def __str__ (self):
        return ('{0}'.format(self.user))
