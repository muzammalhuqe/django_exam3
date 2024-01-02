from django.urls import path, include
from . import views
urlpatterns = [
    # path('add/', views.AddCarCreateView.as_view(), name = 'add_car'),
    path('car/<int:id>', views.DetailCarView.as_view(), name='car_detail'),
    path('buy/<int:id>/', views.BuyCarView.as_view(), name='buy_car'),
]