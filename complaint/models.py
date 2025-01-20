from django.db import models
from Authentication.models import Register

# Create your models here.

class Complaints(models.Model):
    subject = models.CharField(max_length=50,default='')
    message = models.CharField(max_length=500,default='')
    response = models.CharField(max_length=500,null=True)
    responsetime=models.CharField(max_length=50,default='Not Responded')
    status = models.CharField(max_length=100,null=True,default="NULL")
    uid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name='+')
    respondedby = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
