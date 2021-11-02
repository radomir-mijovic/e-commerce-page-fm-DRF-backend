from django.contrib import admin
from .models import *


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'discount']


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Company, CompanyAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(ProductImages)
