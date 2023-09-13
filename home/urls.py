from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('bucket/', views.BucketView.as_view(), name='bucket'),
    path('delete/', views.DeleteObject.as_view(), name='delete-obj'),
    path('category/<slug:category_slug>/', views.HomeView, name='category_filter'),

]
