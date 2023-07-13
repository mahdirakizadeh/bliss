from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class ProductModel(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300, unique=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    descriptions = RichTextField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:detail', args=[self.slug])
