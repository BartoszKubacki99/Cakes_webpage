from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Product

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        labels = {
            'name': '',
            'description': '',
            'estimated_price': '',
            'category': 'Kategoria',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Opis produktu'}),
            'estimated_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cena'}),
        }