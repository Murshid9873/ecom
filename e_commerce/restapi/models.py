from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    age = models.BigIntegerField()
    phone = models.BigIntegerField()
    email = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)