from django.db import models
from Authentication.models import Register
from department.models import *
# Create your models here.

class add_work(models.Model):
    title = models.CharField(max_length=100,default='')
    description = models.CharField(max_length=500,default='')
    date = models.DateField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    status = models.CharField(max_length=500,default='')
    staffid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    update_status = models.CharField(max_length=50,default='')
    message = models.CharField(max_length=500,default='')
    files = models.FileField(default='')
    semester= models.ForeignKey(Semesters,on_delete=models.CASCADE,null=True)
    
class StatusClass(models.Model):
    work = models.ForeignKey(add_work,on_delete=models.CASCADE,null=True)
    update_status = models.CharField(max_length=50,default='')
    message = models.CharField(max_length=500,default='')
    files = models.FileField(default='')
    

    
    
