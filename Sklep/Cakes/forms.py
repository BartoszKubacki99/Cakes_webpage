from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Product, Category, Order, Ingredients

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'last_name', 'description', 'product', 'email', 'phone', 'adress', 'deadline')
        labels = {
            'name': '',
            'last_name': '',
            'description': '',
            'product': 'Produkty:',
            'email': '',
            'phone': '',
            'adress': 'Adres zamieszkania:',
            'deadline': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imię'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwisko'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Opis zamówienia'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Podaj email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nr telefonu'}),
            'adres': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Podaj adres'}),
            'deadline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Data zamówienia: np: 2023-12-15 18:00'}),
        }

class OrderUpdateForm(ModelForm):
    class Meta:
        model = Order
        fields = ('name', 'last_name', 'description', 'product', 'email', 'phone', 'adress', 'deadline', 'status')
        labels = {
            'name': '',
            'last_name': '',
            'description': '',
            'product': 'Produkty:',
            'email': '',
            'phone': '',
            'adress': 'Adres zamieszkania:',
            'deadline': '',
            'status': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Imię'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwisko'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Opis zamówienia'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Podaj email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nr telefonu'}),
            'adres': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Podaj adres'}),
            'deadline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Data zamówienia: np: 2023-12-15 18:00'}),
        }


class IngredientForm(ModelForm):
    class Meta:
        model = Ingredients
        fields = '__all__'
        labels = {
            'name': '',
            'description': '',
            'product': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Opis produktu'}),
            'product': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'W produkcie:'}),
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        labels = {
            'name': '',
            'description': '',
            'estimated_price': '',
            'category': 'Kategoria',
            'product_image': '',
            'ingredients_list': 'Składniki (Przytrzymaj ctrl aby dodać więcej niż jeden składnik)'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nazwa'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Opis produktu'}),
            'estimated_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cena'}),
            'ingredients_list': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {'name': 'Nazwa kategorii'}