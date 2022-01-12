from django.db import models

# Create your models here.

#------------------------------------- ADD PRODUCT -------------------------------------------------
class Productadd(models.Model):
    brandname = models.CharField(max_length= 20)
    hsncode = models.IntegerField(default=0)
    productname = models.CharField(max_length=50)
    productprice = models.IntegerField(default=0)
    actualprice = models.IntegerField(default=0)

#------------------------------------- ADD STOCK ---------------------------------------------------
class Stockadd(models.Model):
    brandname = models.CharField(max_length= 20)
    productname = models.CharField(max_length=50)
    availbags = models.IntegerField(default=0)
    availpieces = models.IntegerField(default=0)