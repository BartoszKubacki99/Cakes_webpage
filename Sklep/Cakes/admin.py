from django.contrib import admin
from .models import WebsiteUser, Category, Product, Ingredients, Order


admin.site.register(WebsiteUser)
admin.site.register(Category)
# #admin.site.register(Product)
admin.site.register(Ingredients)
admin.site.register(Order)




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'estimated_price',)
    ordering = ('name',)
    search_fields = ('name',)


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     fields = (('name'), 'description', 'estimated_price', 'Producer')
#     list_display = ('name',)
#     list_filter = ('name',)
#     ordering = ('name', )

