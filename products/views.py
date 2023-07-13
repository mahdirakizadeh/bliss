from django.shortcuts import render
from .models import ProductModel
from django.views import View
from django.shortcuts import get_object_or_404


class ProductView(View):
    def get(self, request):
        products = ProductModel.objects.all()
        return render(request, 'products/service.html', {'products': products})


class DetailProductView(View):
    def get(self, request, slug_product):
        product = get_object_or_404(ProductModel, slug=slug_product)
        return render(request, 'products/servicedetail.html', {'product': product})
