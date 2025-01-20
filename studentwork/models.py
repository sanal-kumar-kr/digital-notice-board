from django.db import models
from Authentication.models import Register

# Create your models here.

class student_add_work(models.Model):
    title = models.CharField(max_length=100,default='')
    description = models.CharField(max_length=500,default='')
    date = models.DateField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    status = models.CharField(max_length=500,default='Not assigned')
    update_status = models.CharField(max_length=50,default='')
    staffid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    message = models.CharField(max_length=500,default='')
    files = models.FileField(null=True)
    