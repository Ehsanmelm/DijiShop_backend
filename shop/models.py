from django.db import models
from django.conf import settings

# Create your models here.

class SellerModel(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)


class StoreModel(models.Model):
    name = models.CharField(max_length= 255)
    address = models.TextField()
    # logo = models.ImageField(upload_to=)

class StuffModel(models.Model):
    store = models.ForeignKey(StoreModel , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    capacity = models.IntegerField()
    # image = models.ImageField(upload_to=)

