from django.db import models


class adduserModel(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    contactNumber = models.BigIntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
  

    def __str__(self):
        return self.username
