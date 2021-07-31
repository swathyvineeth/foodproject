from django.shortcuts import render,get_object_or_404
from .models import Category,Product


# Create your views here.

def catfunction(request,c_slug=None):
    c_page=None
    prod=None
    if c_slug!=None:
        c_page=get_object_or_404(Category,slug=c_slug)
        prod=Product.objects.filter(category=c_page,available=True)
    else:
        prod=Product.objects.all().filter(available=True)
    cat=Category.objects.all()

    return render(request,"index.html",{"cat":cat,"prod":prod})
def profunction(request,c_slug,product_slug):
    try:

        prod=Product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,"item.html",{"prod":prod})
