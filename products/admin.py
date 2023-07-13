from django.contrib import admin
from .models import ProductModel


class ProductModelAdmin(admin.ModelAdmin):
    ordering = ('name', 'created')
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(ProductModel, ProductModelAdmin)
