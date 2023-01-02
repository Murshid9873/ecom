from django.db import models

# Create your models here.

class Customer(models.Model):
    Customer_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100, default= '')
    password = models.CharField(max_length=50)

class Seller(models.Model):
    seller_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    company_name = models.CharField(max_length=50)
    acc_holder_name = models.CharField(max_length=50)
    ifsc = models.CharField(max_length=25, default= '')
    branch = models.CharField(max_length=50)
    acc_no = models.BigIntegerField()
    upload = models.ImageField(upload_to='seller/', default= '')
    user_name = models.CharField(max_length=150, default= '')
    password = models.CharField(max_length=50, default='')
    