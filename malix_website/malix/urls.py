from django.urls import path
from .views import my_view
app_name = 'malix'

urlpatterns = [
    path('', my_view, name='index'),
]