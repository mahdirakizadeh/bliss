from django.shortcuts import render
from .models import ProductModel, CategoryModel
from django.views import View
from django.shortcuts import get_object_or_404


class ProductView(View):
    def get(self, request, category_slug=None):
        products = ProductModel.objects.filter(available=True)
        categories = CategoryModel.objects.filter(is_sub=False)
        if category_slug:
            category = CategoryModel.objects.get(slug=category_slug)
            products = products.filter(category=category)
        return render(request, 'products/service.html', {'products': products, 'categories': categories})


class DetailProductView(View):
    def get(self, request, slug_product):
        product = get_object_or_404(ProductModel, slug=slug_product)
        return render(request, 'products/service-detail.html', {'product': product})
