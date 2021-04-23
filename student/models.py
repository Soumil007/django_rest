from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 200)
    rollno = models.IntegerField(default = 100)
    age = models.IntegerField(default = 19)
    gender = models.CharField(max_length = 1)
