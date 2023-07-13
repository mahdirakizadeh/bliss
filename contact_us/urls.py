from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('contact_us/', views.ContactView.as_view(), name='contact_us')
]
