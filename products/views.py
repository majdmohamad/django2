from django.shortcuts import render
from .models import Products
# Create your views here.
def product(request):
    return render(request,'products/product.html')
def products(request):
    return render(request,'products/products.html',{'pro':Products.objects.all(),'current_page':'products'})