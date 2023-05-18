from django.shortcuts import render
from ekart.form import CustomUserForm
from .models import *
from django.contrib import messages
from django.shortcuts import redirect




def home (request):
    products=Product.objects.filter(trending=1)
    return render(request,"ekart/index.html",{"products":products})

def login (request):
   return render(request,"ekart/login.html")


def register(request):
    form=CustomUserForm()
    if request.method=='POST':
      form=CustomUserForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('/login')
    
    return render(request,"ekart/register.html",{'form':form})

def collections(request):
    category=Category.objects.filter(status=0)
    return render(request,"ekart/collections.html",{"category":category})
def collectionsview(request,name):
    if(Category.objects.filter(name=name,status=0)):
        products=Product.objects.filter(category__name=name)
        return render(request,"ekart/products/index.html",{"products":products,"category_name":name})
    else:
        messages.warning(request,"No Such Category Found")
        return redirect ('collections')

def product_details(request,cname,pname):
     if(Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"ekart/products/product_details.html",{"products":products})
        else:
            messages.error(request,"No Such Products Found")
            return redirect('collections')
     else:
        messages.error(request,"No Such Category Found")
        return redirect('collections')
    