from django.contrib.auth.models import AbstractUser, User
from django.db import models


IS_ACTIVE = [
    (1, 'W trakcie przetwarzania'),
    (2, 'Zamówienie zatwierdzone! Skontaktujemy się z tobą w ciągu dwóch dni!'),
    (3, 'Niestety nie jesteśmy w stanie zrealizować twojego zamówienia, \
    o więcej informacji zgłoś się do naszej obsługi klienta.'),
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


class Ingredients(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name



class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    estimated_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_image = models.ImageField(null=True, blank=True, upload_to="images/")
    ingredients_list = models.ManyToManyField(Ingredients, blank=True)
    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name='Imię')
    last_name = models.CharField(max_length=100, verbose_name='Nazwisko')
    description = models.TextField(blank=True, verbose_name='Opis')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, verbose_name='produkt')
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=100, verbose_name='numer telefonu:')
    adress = models.TextField(verbose_name='adres zamieszkania')
    deadline = models.DateTimeField('Order_date')
    status = models.IntegerField(choices=IS_ACTIVE, blank=True, null=True, default=1)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    website_users = models.ForeignKey(WebsiteUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name + ' ' + self.last_name
