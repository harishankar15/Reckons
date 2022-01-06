from django.db import models


class addproductModel(models.Model):
    brandname = models.CharField(max_length=20)
    productname = models.CharField(max_length=20)
    productcode = models.CharField(max_length=20)
    productprice = models.IntegerField()
    actualprice = models.IntegerField()
    def __str__(self):
        return self.productname
  
