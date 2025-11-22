from django.urls import path
from . import views #import from actual folder

# /products
# /products/1/detail
# /products/new
# ...

urlpatterns = [
    path('', views.index),
    path('new', views.new_products)
]