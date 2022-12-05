from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100,blank=True)
    roll=models.IntegerField(default=0)
    city=models.CharField(max_length=100,blank=True)