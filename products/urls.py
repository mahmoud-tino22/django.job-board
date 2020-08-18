from django.urls import path
from . import views

urlpatterns = [
    path( 'product' ,views.product ,name='product'),
    path( 'allproducts' ,views.allproducts ,name='allproducts'),
    path( 'search' ,views.search ,name='search'),


]