from django.db import models

# Create your models here.

class Departments(models.Model):
    departmentname = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=200,default='')
    departmentimage = models.FileField(default='')
    def __str__(self) -> str:
        return self.departmentname
    
class Semesters(models.Model):
    semestername = models.CharField(max_length=100)
    department = models.ForeignKey(Departments,on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.semestername