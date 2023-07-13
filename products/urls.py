from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('products/', views.ProductView.as_view(), name='product'),
    path('<slug:slug_product>/', views.DetailProductView.as_view(), name='detail'),
]

