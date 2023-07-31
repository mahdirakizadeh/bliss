from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('category/<slug:category_slug>/', views.ProductView.as_view(), name='category_filter'),
    path('products/', views.ProductView.as_view(), name='product'),
    path('<slug:slug_product>/', views.DetailProductView.as_view(), name='detail'),
]

