from django.urls import path, include
from . import views

urlpatterns = [
    path('order_history/', views.OrderHistoryView.as_view(), name='order_history'),
]