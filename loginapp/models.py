from django.db import models
from datetime import datetime
# Create your models here.


class Student(models.Model):
    studEmail = models.EmailField(max_length=20, default="")
    studUsername = models.TextField(max_length=20, default="")
    studFName = models.TextField(max_length=20, default="")
    studLName = models.TextField(max_length=20, default="")
    studAge = models.IntegerField(default=0,null=True,blank=True)
    studAddress = models.TextField(max_length=50, default="")
    studClass = models.IntegerField(default=0,null=True,blank=True)
    studPassword = models.TextField(max_length=20, default="")
    studBirthdate = models.DateField(default=datetime.now(),null=True,blank=True)

    def __str__(self) -> str:
        return self.studUsername

