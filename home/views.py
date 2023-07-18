from django.shortcuts import render
from django.views import View
from blog.models import BlogModel, Image
from contact_us.forms import ContactForm


def HomeView(request):
    blog = BlogModel.objects.all()
    imgb = Image.objects.all()
    contact = ContactForm()
    return render(request, 'home/index.html', {'blog': blog, 'imgb': imgb, 'contact': contact})
