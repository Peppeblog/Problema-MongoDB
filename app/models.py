from django.db import models
from djongo.models.fields import ObjectIdField
from django.contrib.auth.models import User

class Profile(models.Model):
    _id = ObjectIdField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Order(models.Model):
    _id = ObjectIdField()
    #profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
   #datetime = models.DatetimeField(auto_now_add=True)
    price = models.FloatField()
    quantity = models.FloatField()
