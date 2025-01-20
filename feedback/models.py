from django.db import models
from Authentication.models import Register

# Create your models here.
class Feedbacks(models.Model):
    subject = models.CharField(max_length=50,default='')
    message = models.CharField(max_length=500,default='')
    response = models.CharField(max_length=500,null=True)
    status = models.CharField(max_length=100,null=True,default="Not Responded")
    uid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
