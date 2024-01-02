from django.db import models

# Create your models here.

class CarBrand(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique = True, blank=True, null=True)

    def __str__(self):
        return self.name


class CarDetails(models.Model):
    brand = models.ForeignKey(CarBrand, on_delete = models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length = 20)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'car_details/media/uploads/', blank=True, null=True)

    def __str__(self) :
        return f"Car : {self.name}, Brand : {self.brand.name}"
    

class Comment(models.Model):
    car = models.ForeignKey(CarDetails, on_delete = models.CASCADE, related_name = 'comments')
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"Comment by {self.name}"
