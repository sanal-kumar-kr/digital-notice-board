from django.db import models

# Create your models here.
class Classes(models.Model):
    classname = models.CharField(max_length=50,default='')
    seatrows = models.IntegerField(default='')
    seatcolumns = models.IntegerField(default='')
    strength = models.IntegerField(null=True)
    def __str__(self) -> str:
        return self.classname
    