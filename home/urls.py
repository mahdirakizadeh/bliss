from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('category/<slug:category_slug>/', views.HomeView, name='category_filter'),
]
