from django.contrib import admin
from django.urls import path
from .views import HomeView, ProductsListView, AddProductView,\
    CategoryView, Show_categoryView, SearchProductView, ShowProductView, AllProductsView,\
    UpdateProductView, DeleteProductView, AddCategoryView, AddOrderView, MyOrderView, \
    OrderAdminView, UpdateOrder, DeleteOrderView, UpdateCategoryView, DeleteCategoryView,\
    UpdateAdminOrderView, IngredientsListView, UpdateIngredientView, DeleteIngredientView,\
    AddIngredientView, ShowIngredientView


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
    path('category_update/<category_id>/', UpdateCategoryView, name='update-category'),
    path('delete_category/<category_id>', DeleteCategoryView, name='delete-category'),
    path('show_category/<category_id>/', Show_categoryView, name='show-category'),
    path('search/', SearchProductView, name='search-product-list'),
    path('AddOrder/', AddOrderView, name='add-order'),
    path('orderadminview/', OrderAdminView, name='order-view'),
    path('my_order_view/', MyOrderView, name='my-order-view'),
    path('update_order/<order_id>/', UpdateOrder, name='update-order'),
    path('update_admin_order/<order_id>/', UpdateAdminOrderView, name='update-admin-order'),
    path('delete_order/<order_id>', DeleteOrderView, name='delete-order'),
    path('ingredientslist/', IngredientsListView,  name='ingredients-list'),
    path('update_ingredient/<ingredient_id>/', UpdateIngredientView, name='update-ingredient'),
    path('delete_ingredient/<ingredient_id>/', DeleteIngredientView, name='delete-ingredient'),
    path('add_ingredient/', AddIngredientView, name='add-ingredient'),
    path('show_ingredient/<ingredient_id>/', ShowIngredientView, name='show-ingredient'),
]