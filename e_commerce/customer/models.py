from django.db import models
from common.models import Customer
from reseller.models import Product

# Create your models here.

class cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    Product = models.ForeignKey(Product, on_delete = models.CASCADE)
