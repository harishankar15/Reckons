from django.db import models


class addstockModel(models.Model):
    brandname = models.CharField(max_length=20)
    productname = models.CharField(max_length=20)
    availableBags = models.IntegerField()
    availablePieces = models.BigIntegerField()
  

    def __str__(self):
        return self.productname
