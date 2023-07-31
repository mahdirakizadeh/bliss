from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField


class CategoryModel(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subcategory',
                                     null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=300)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:category_filter', args=[self.slug])


class ProductModel(models.Model):
    category = models.ManyToManyField(CategoryModel, related_name='products')
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=300, unique=True)
    image = models.ImageField(upload_to='media', null=True, blank=True)
    descriptions = RichTextField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:detail', args=[self.slug])
