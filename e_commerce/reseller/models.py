from django.db import models
from common.models import Seller

# Create your models here.

class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete = models.CASCADE)
    p_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    p_no = models.BigIntegerField()
    upload = models.ImageField(upload_to='product/', default= '')
    price =   models.FloatField()
    stock = models.ImageField()