from django.contrib import admin
from .models import BlogModel, Image


class ImageInline(admin.StackedInline):
    model = Image
    extra = 2


class ExtendedBlogModelAdmin(admin.ModelAdmin):
    ordering = ('title', 'created')
    prepopulated_fields = {'slug': ('title',)}
    inlines = (ImageInline, )


admin.site.register(BlogModel, ExtendedBlogModelAdmin)
