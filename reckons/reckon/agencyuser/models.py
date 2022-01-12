from django.db import models

# Create your models here.

class Productadd(models.Model):
    brandname = models.CharField(max_length= 20)
    hsncode = models.IntegerField(default=0)
    productname = models.CharField(max_length=50)
    productprice = models.IntegerField(default=0)
    actualprice = models.IntegerField(default=0)

class Stockadd(models.Model):
    brandname = models.ForeignKey(Productadd,models.DO_NOTHING,related_name='sto_brandname',db_column='agencyuser_brandname')
    productname = models.ForeignKey(Productadd,models.DO_NOTHING,related_name='sto_productname',db_column='agencyuser_productname')
    # brandname = models.CharField(max_length= 20)
    # productname = models.CharField(max_length=50)
    availbags = models.IntegerField(default=0)
    availpieces = models.IntegerField(default=0)