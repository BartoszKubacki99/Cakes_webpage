from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.http import HttpResponseRedirect
from .forms import CreateUserForm, ProductForm
from django.contrib.auth import authenticate, login, logout
from .models import Product, Category


def DeleteProductView(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('products-list')


def UpdateProductView(request, product_id):
    product = Product.objects.get(pk=product_id)
    form = ProductForm(request.POST or None, instance=product)
    context = {'product': product,
               'form': form}
    if form.is_valid():
        form.save()
        return redirect('products-list')
    return render(request, 'Shop/update_product.html', context)


def SearchProductView(request):
    if request.method == "POST":
        searched = request.POST['searched']
        Products = Product.objects.filter(name__contains=searched)
        return render(request, 'Shop/search_product.html', {'searched': searched, 'Products': Products})
    else:
        return render(request, 'Shop/search_product.html', {})


def Show_categoryView(request, category_id):
    products = Product.objects.get(pk=category_id)
    context = {'products': products,
               }
    return render(request, 'Shop/Show_category.html', context)


def CategoryView(request):
    category_list = Category.objects.all().order_by('name')
    context = {'category_list': category_list}
    return render(request, 'Shop/Category.html', context)


def AllProductsView(request):
    all_products = Product.objects.all()
    context = {'all_products': all_products}
    return render(request, 'Shop/all_products.html', context)


def ProductsListView(request):
    products_list = Product.objects.all().order_by('name')
    context = {'products_list': products_list}
    return render(request, 'Shop/ProductList.html', context)

def ShowProductView(request, product_id):
    product = Product.objects.get(pk=product_id)
    context = {'product': product}
    return render(request, 'Shop/show_product.html', context)


def HomeView(request):
    return render(request, 'Shop/home.html', {})


def AddProductView(request):
    submitted = False
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addproduct?submitted=True')
    else:
        form = ProductForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'Shop/Add_product.html',
                  {'form': form,
                   'submitted': submitted}
                  )

def AddCategoryView(request):
    model = Category
    return render(request, 'Shop/Add_category.html')