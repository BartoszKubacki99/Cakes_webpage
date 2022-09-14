from django.contrib import admin
from django.urls import path
from .views import HomeView, ProductsListView, AddProductView,\
    CategoryView, Show_categoryView, SearchProductView, ShowProductView, AllProductsView,\
    UpdateProductView, DeleteProductView, AddCategoryView

urlpatterns = [
    path('', HomeView, name='home'),
    path('home/', HomeView),
    path('productslist/', ProductsListView, name='products-list'),
    path('show_products/<product_id>/', ShowProductView, name='show-product'),
    path('update_products/<product_id>/', UpdateProductView, name='update-product'),
    path('delete_product/<product_id>', DeleteProductView, name='delete-product'),
    path('allproducts/', AllProductsView, name='all-products'),
    path('addproduct/', AddProductView, name='add-product'),
    path('category/', CategoryView, name='category-list'),
    path('addcategory/', AddCategoryView, name='add-category'),
    path('show_category/<category_id>/', Show_categoryView, name='show-category'),
    path('search/', SearchProductView, name='search-product-list'),

]