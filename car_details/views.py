from django.shortcuts import render, redirect, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . import forms
from . import models
from order_handle.models import Order
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import DetailView
from car_details.models import CarDetails
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class DetailCarView(DetailView):
    model = CarDetails
    template_name = 'car_details.html'
    pk_url_kwarg = 'id'
    context_object_name = 'car_details'


    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data = self.request.POST)
        car  = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.car = car
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()

        
        comment_form = forms.CommentForm()

        context ['comments'] = comments
        context ['comment_form'] = comment_form
        return context
    
@method_decorator(login_required, name = 'dispatch')
class BuyCarView(LoginRequiredMixin, View):
    def get(self, request, id):
        car = get_object_or_404(CarDetails, pk=id)
        if car.quantity > 0:
            order = Order(user=request.user, car=car)
            order.save()
            car.quantity -= 1
            car.save()
            return redirect('order_history')
        else:
            return render(request, 'out_of_stock.html')
    


