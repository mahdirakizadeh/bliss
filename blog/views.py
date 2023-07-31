from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404
from .models import BlogModel, Image


class BlogView(View):
    def get(self, request):
        blog = BlogModel.objects.all()
        imgb = Image.objects.all()
        return render(request, 'blog/blog.html', {'blog': blog, 'imgb': imgb})


class BolgDetail(View):
    def get(self, request, blog_slug):
        blog = get_object_or_404(BlogModel, slug=blog_slug)
        return render(request, 'blog/blogdetail.html', {'blog': blog})
