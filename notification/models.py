from django.db import models
from Authentication.models import Register


class Notifications(models.Model):
    title = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=500,default='')
    date = models.DateField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    staffid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    usertype = models.CharField(max_length=500,default='')
    
class StaffNotifications(models.Model):
    title = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=500,default='')
    date = models.DateField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    staffid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    usertype = models.CharField(max_length=500,default='')
    
class StudentNotifications(models.Model):
    title = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=500,default='')
    date = models.DateField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    staffid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)