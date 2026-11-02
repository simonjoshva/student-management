from django.db import models
class student(models.Model):
    idno=models.IntegerField()
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    course=models.CharField(max_length=100)
    email=models.CharField(max_length=50)

# Create your models here.
