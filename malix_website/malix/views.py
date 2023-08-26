from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

# Create your views here.

def my_view(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def single(request):
    return render(request,'single.html')
def service(request):
    return render(request,'service.html')
def price(request):
    return render(request,'pricing.html')
def contact(request):
    return render(request,'contact.html')
def blog(request):
    return render(request,'blog.html')