from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

# Create your views here.

def my_view(request):
    return render(request, 'index.html')
