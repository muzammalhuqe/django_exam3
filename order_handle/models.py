from django.db import models
from django.contrib.auth.models import User
from car_details.models import CarDetails
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    car = models.ForeignKey(CarDetails, on_delete = models.CASCADE)

    def __str__(self):
        return self.user