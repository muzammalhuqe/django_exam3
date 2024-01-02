from django import forms
from .models import Comment, CarBrand,CarDetails

class AddCarBrandForm(forms.ModelForm):
    class Meta: 
        model = CarBrand
        fields = '__all__'

class AddCarDetailsForm(forms.ModelForm):
    class Meta: 
        model = CarDetails
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'email', 'body']