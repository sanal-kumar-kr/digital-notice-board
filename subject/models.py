from django.db import models
from department.models import *
from Authentication.models import Register

# Create your models here.
class Subjects(models.Model):
    name = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=500,default='')
    department = models.ForeignKey(Departments,on_delete=models.CASCADE,null=True)
    semester = models.ForeignKey(Semesters,on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.name
 
class Notes(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    notes = models.FileField(null=True)

    staffid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    department = models.ForeignKey(Departments,on_delete=models.CASCADE,null=True)
    semester= models.ForeignKey(Semesters,on_delete=models.CASCADE,null=True)


   
    def __str__(self) -> str:
        return self.title        
    