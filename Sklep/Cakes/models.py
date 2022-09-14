from django.contrib.auth.models import AbstractUser, User
from django.db import models


IS_ACTIVE = [
    ('1', 'yes'),
    ('2', 'no'),
]


class WebsiteUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ManyToManyField(Category)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    estimated_price = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.name


class Image(models.Model):
    name = models.CharField(max_length=100)
    path = models.ImageField()
    description = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    product = models.ManyToManyField(Product)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name='Imię')
    last_name = models.CharField(max_length=100, verbose_name='Nazwisko')
    description = models.TextField(blank=True, verbose_name='Opis')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, verbose_name='produkt')
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, verbose_name='numer telefonu:')
    adress = models.TextField(verbose_name='adres zamieszkania')
    deadline = models.DateTimeField(auto_now=True, verbose_name='Data')
    status = models.IntegerField(choices=IS_ACTIVE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Wykonawca')

    def __str__(self):
        return self.name + ' ' + self.last_name
