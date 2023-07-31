from django.contrib import admin
from .models import ProductModel, CategoryModel


class ProductModelAdmin(admin.ModelAdmin):
    raw_id_fields = ('category',)
    ordering = ('name', 'created')
    prepopulated_fields = {'slug': ('name', )}


class CategoryModelAdmin(admin.ModelAdmin):
    list_filter = ('is_sub',)
    list_display = ('name', 'is_sub')
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(ProductModel, ProductModelAdmin)

