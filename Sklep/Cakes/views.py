import json

from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import ProductForm, CategoryForm, OrderForm, OrderUpdateForm, IngredientForm
from .models import Product, Category, Order, Ingredients





def IngredientsListView(request):
    ingredients_list = Ingredients.objects.all()
    return render(request, 'Shop/Ingredients_list.html', {'ingredients_list': ingredients_list})


def ShowIngredientView(request, ingredient_id):
    Ingredient = Ingredients.objects.get(pk=ingredient_id)
    product_list = Product.objects.filter(ingredients_list=ingredient_id)
    context = {'Ingredient': Ingredient,
               'product_list': product_list,
               }
    return render(request, 'Shop/show_ingredient.html', context)

def AddIngredientView(request):
    submitted = False
    if request.method == "POST":
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_ingredient?submitted=True')
    else:
        form = IngredientForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'Shop/Add_Ingredients.html',
                  {'form': form,
                   'submitted': submitted}
                  )


def UpdateIngredientView(request, ingredient_id):
    ingredient = Ingredients.objects.get(pk=ingredient_id)
    form = IngredientForm(request.POST or None, instance=ingredient)
    context = {'ingredient': ingredient,
               'form': form}
    if form.is_valid():
        form.save()
        return redirect('ingredients-list')

    return render(request, 'Shop/update_ingredients.html', context)


def DeleteIngredientView(request, ingredient_id):
    ingredient = Ingredients.objects.get(pk=ingredient_id)
    ingredient.delete()
    return redirect('ingredients-list')



def UpdateOrder(request, order_id):
    order = Order.objects.get(pk=order_id)
    form = OrderForm(request.POST or None, instance=order)
    context = {'order': order,
               'form': form}
    if form.is_valid():
        form.save()
        return redirect('my-order-view')

    return render(request, 'Shop/update_order.html', context)


def UpdateAdminOrderView(request, order_id):
    order = Order.objects.get(pk=order_id)
    form = OrderUpdateForm(request.POST or None, instance=order)
    context = {'order': order,
               'form': form}
    if form.is_valid():
        form.save()
        return redirect('my-order-view')

    return render(request, 'Shop/update_admin_order.html', context)


def DeleteOrderView(request, order_id):
    order = Order.objects.get(pk=order_id)
    order.delete()
    return redirect('my-order-view')


def MyOrderView(request):
    if request.user.is_authenticated:
        me = request.user.id
        orders = Order.objects.filter(manager=me)
        return render(request, 'Shop/My_orders.html', {"me": me, "orders": orders})
    else:
        messages.success(request, ("Nie możesz zobaczyć tej strony "))
        return redirect('home')


def OrderAdminView(request):
    orders_list = Order.objects.all()
    context = {'orders_list': orders_list}
    return render(request, 'Shop/OrderAdmin.html', context)


def AddOrderView(request):
    submitted = False
    if request.method == "POST":
        if request.user.is_superuser:
            form = OrderUpdateForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/AddOrder?submitted=True')
        else:
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.manager = request.user
                order.save()
                return HttpResponseRedirect('/AddOrder?submitted=True')
    else:
        if request.user.is_superuser:
            form = OrderUpdateForm
        else:
            form = OrderForm

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'Shop/AddOrder.html',
                      {'form': form,
                       'submitted': submitted}
                      )


def DeleteProductView(request, product_id):
    product = Product.objects.get(pk=product_id)
    product.delete()
    return redirect('products-list')


def UpdateProductView(request, product_id):
    product = Product.objects.get(pk=product_id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
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
        context = {'searched': searched,
                   'Products': Products,
                   }
        return render(request, 'Shop/search_product.html', context)
    else:
        return render(request, 'Shop/search_product.html', {})


def Show_categoryView(request, category_id):
    categories = Product.objects.filter(category=category_id)
    category = Category.objects.get(pk=category_id)
    context = {'categories': categories,
               'category': category,
               }
    return render(request, 'Shop/Show_category.html', context)


def CategoryView(request):
    category_list = Category.objects.all()
    context = {'category_list': category_list}
    return render(request, 'Shop/Category.html', context)


def UpdateCategoryView(request, category_id):
    category = Category.objects.get(pk=category_id)
    form = CategoryForm(request.POST or None, request.FILES or None, instance=category)
    context = {'category': category,
               'form': form}
    if form.is_valid():
        form.save()
        return redirect('category-list')
    return render(request, 'Shop/update_category.html', context)


def DeleteCategoryView(request, category_id):
    category = Category.objects.get(pk=category_id)
    category.delete()
    return redirect('category-list')


def AddCategoryView(request):
    submitted = False
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/addcategory?submitted=True')
    else:
        form = CategoryForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'Shop/Add_category.html',
                  {'form': form,
                   'submitted': submitted}
                  )


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


def AddProductView(request):
    submitted = False
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
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


def HomeView(request):
    return render(request, 'Shop/home.html', {})
