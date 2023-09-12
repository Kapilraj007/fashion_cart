from django.http import  JsonResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import CustomUserForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
import json
def home(request):
    products=Product.objects.filter(trending=1)
    return render(request,"index.html",{'products':products})
def login_page(request):
     if request.user.is_authenticated:
        return redirect('Home')
     else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Login successfully")
                return redirect('Home')
            else:
                messages.error(request,"Invaild username or password")
                return redirect('login')
                
        return render(request,'login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,"logged out successfuly")
        return redirect('Home')

@csrf_exempt
def register(request):
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Regirations successfully')
            return redirect('login')
    return render(request,"register.html",{'form':form})
def collections(request):
    category=Category.objects.filter(status=0)
    return render(request,"collections.html",{'catagory':category})

def collectionsview(request,name):
  if(Category.objects.filter(name=name,status=0)):
      products=Product.objects.filter(Category__name=name,status=0)
      print(products)    
      return render(request,"products/index.html",{"products":products, "category_name":name})
  else:
    messages.warning(request,"No Such Catagory Found")
    return redirect('Collections')

def productdetails(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"products/product_details.html",{"products":products})
        else:
            messages.warning(request,"No product found")
            return redirect('Collections')
    else:
        messages.warning(request,"No category found")
        return redirect('collections')

def add_to_cart(request):
    if request.headers.get('x-requested-with')=='XMLHttpRequest':
        if request.user.is_authenticated:
            data=json.load(request)
            product_qty=data['product_qty']
            product_id=data['pid']
            #print(request.user.id)
            product_status=Product.objects.get(id=product_id)
            if product_status:
                 if Cart.objects.filter(user=request.user.id,product_id=product_id):
                      return JsonResponse({'status':'Product Already in Cart'}, status=200)
                 else:
                     if product_status.quantity>=product_qty:
                        Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
                        return JsonResponse({'status':'Product Added to Cart'}, status=200)
                     else:
                         return JsonResponse({'status':'Product Stock Not Available'}, status=200)
        else:
             return JsonResponse({'status':'Login to Add Cart'}, status=200)
    else:
       return JsonResponse({'status':'Invalid Access'}, status=200)


def cart_page(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        return render(request ,"products/cart.html",{'cart':cart})
    else:
        return redirect('Home')

def removecart(request,cid):
    cart=Cart.objects.get(id=cid)
    cart.delete()
    return redirect('cart')

def fav_page(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_id=data['pid']
      product_status=Product.objects.get(id=product_id)
      if product_status:
         if Favourite.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Favourite'}, status=200)
         else:
          Favourite.objects.create(user=request.user,product_id=product_id)
          return JsonResponse({'status':'Product Added to Favourite'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Favourite'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)

def favviewpage(request):
  if request.user.is_authenticated:
    fav=Favourite.objects.filter(user=request.user)
    return render(request,"products/fav.html",{"fav":fav})
  else:
    return redirect("/")
 
def remove_fav(request,fid):
  item=Favourite.objects.get(id=fid)
  item.delete()
  return redirect("/favviewpage")
