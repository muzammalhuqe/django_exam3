from django.shortcuts import render
from car_details.models import CarDetails
from car_details.models import CarBrand
def home(request, car_slug = None):

    data = CarDetails.objects.all()
    if car_slug is not None:
        car = CarBrand.objects.get(slug = car_slug)
        data = CarDetails.objects.filter(brand = car)
    car_brand = CarBrand.objects.all()
    return render(request, 'home.html', {'data' : data, 'car_brand' : car_brand})