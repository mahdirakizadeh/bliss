from django.shortcuts import render
from django.views import View


def HomeView(request):
    return render(request, 'home/index.html')
