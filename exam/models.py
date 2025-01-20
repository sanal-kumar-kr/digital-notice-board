from django.db import models
from department.models import *
from subject.models import *
from Authentication.models import Register
from classroom.models import *
from exam.models import *


# Create your models here.
class Exams(models.Model):
    examname = models.CharField(max_length=50)
    date = models.DateField(default='') 
    start_time = models.TimeField(default='')
    end_time = models.TimeField(default='')
    department = models.ForeignKey(Departments,on_delete=models.CASCADE,null=True)
    semester = models.ForeignKey(Semesters,on_delete=models.CASCADE,null=True)
    subject = models.ForeignKey(Subjects,on_delete=models.CASCADE,null=True)
    examstatus = models.IntegerField(default=0)

    
    def __str__(self) -> str:
        return self.examname
   