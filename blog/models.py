from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class BlogModel(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(max_length=200, unique=True)
    body = RichTextField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[self.slug])


class Image(models.Model):
    bolg = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='blogo')
    image = models.ImageField(upload_to='media', null=True, blank=True)
