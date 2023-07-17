from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blogs/', views.BlogView.as_view(), name='blog'),
    path('details/<slug:blog_slug>/', views.BolgDetail.as_view(), name='blog_detail'),
]
