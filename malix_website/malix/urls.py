from django.urls import path
from .views import my_view, about, single, service, price, contact, blog
app_name = 'malix'

urlpatterns = [
    path('', my_view, name='index'),
    path('about/', about, name='about-page'),
    path('single/', single, name='single'),
    path('service/', service, name='service'),
    path('price/', price, name='pricing_page'),
    path('contact/', contact, name='contact-page'),
    path('blog/', blog, name='blog-page')
]
