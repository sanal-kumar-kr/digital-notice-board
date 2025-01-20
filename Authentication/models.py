from django.db import models
from department.models import *

from django.contrib.auth.models import AbstractUser

class Register(AbstractUser):
    name = models.CharField(max_length=50,default='')
    contact = models.IntegerField(null=True)
    address = models.CharField(max_length=50,default='')
    gender = models.CharField(max_length=50,default='')
    experience = models.CharField(max_length=50,default=''  )
    qualification = models.CharField(max_length=50,default='')
    usertype = models.IntegerField(null=True)
    department = models.ForeignKey(Departments,on_delete=models.CASCADE,null=True)
    semester = models.ForeignKey(Semesters,on_delete=models.CASCADE,null=True)
    batch = models.CharField(max_length=50,default='')
    dob = models.CharField(max_length=50,default='')
    status = models.IntegerField(default=0)
    examstatus = models.IntegerField(default=0)
    regno = models.IntegerField(null=True,unique=True)
        
    def __str__(self) -> str:
        return self.name
    class Meta:
        unique_together = ('username', 'regno')
    