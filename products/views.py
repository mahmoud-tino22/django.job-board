from django.shortcuts import render

# Create your views here.
def product(request):
    return render(request ,'products/product.html')

def allproducts(request):
    return render(request ,'products/products.html')

def search(request):
    return render(request , 'products/search.html')

