from django.urls import path
from .views import my_view, about
app_name = 'malix'

urlpatterns = [
    path('', my_view, name='index'),
    path('about/', about, name='about-page')
]