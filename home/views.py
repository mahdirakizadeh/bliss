from django.shortcuts import render
from django.views import View
from blog.models import BlogModel, Image
from products.models import ProductModel, CategoryModel
from contact_us.forms import ContactForm
from .task import all_bucket_object_task, delete_single_object_task


def HomeView(request, category_slug=None):
    blog = BlogModel.objects.all()
    imgb = Image.objects.all()
    contact = ContactForm()
    products = ProductModel.objects.filter(available=True)
    categories = CategoryModel.objects.filter(is_sub=False)
    if category_slug:
        category = CategoryModel.objects.get(slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'home/index.html', {'blog': blog, 'imgb': imgb, 'contact': contact, 'products': products,
                                               'categories': categories})


class BucketView(View):
    def get(self, request):
        object = all_bucket_object_task()
        print("5" * 85)
        print(object)
        return render(request, 'home/bucket.html', {'object': object})


class DeleteObject(View):
    def get(self, request):
        obj = delete_single_object_task()
        print("6" * 69)
        print(obj)
        return obj
        # return render(request, 'home/bucket.html', {'obj': obj})
