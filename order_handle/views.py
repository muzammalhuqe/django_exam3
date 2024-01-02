from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order

@method_decorator(login_required, name = 'dispatch')
class OrderHistoryView(LoginRequiredMixin, View):
    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        # return render(request, 'order_history.html', {'orders': orders})
        return render(request, 'profile.html', {'orders': orders})