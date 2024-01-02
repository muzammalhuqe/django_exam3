from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from . import forms
from django.contrib import messages
from order_handle.models import Order


class SignUpView(CreateView):
    form_class = RegistrationForm
    template_name = 'user_singup.html'
    success_url = reverse_lazy('singup')


class UserLoginView(LoginView):
    template_name = 'user_login.html'
    def get_success_url(self):
        return reverse_lazy('profile')

class UserLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('login')
    

def profile(request):
    orders = Order.objects.filter(user=request.user)
    # return render(request, 'order_history.html', {'orders': orders})
    return render(request, 'profile.html', {'orders': orders})



def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html', {'form' : profile_form})