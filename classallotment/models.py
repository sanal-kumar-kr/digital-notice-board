from department.models import *
from Authentication.models import Register
from classroom.models import *
from exam.models import *
from subject.models import *

class ClassAllotments(models.Model):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semesters, on_delete=models.CASCADE, null=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE, null=True)
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE, null=True)
    classroom = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True, related_name='+')
    staff = models.ForeignKey(Register, on_delete=models.CASCADE, null=True)
    strength = models.ForeignKey(Classes, on_delete=models.CASCADE, null=True)
    status = models.IntegerField(default=0)
    def __str__(self):
        return str(self.strength)

class Allot(models.Model):
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE, null=True)
    staff = models.ForeignKey(Register,on_delete=models.CASCADE,null=True,related_name='+')
    student = models.ManyToManyField(Register)
    classroom = models.ForeignKey(ClassAllotments, on_delete=models.CASCADE, null=True)
    row = models.IntegerField(null=True)
    column = models.IntegerField(null=True)
    
