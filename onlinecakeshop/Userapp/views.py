from django.shortcuts import render,HttpResponse,redirect
from MyAdmin.models import Category,Cake
from django.contrib import messages
from . models import UserMaster,MyCart

# Create your views here.
def home(request):
   categories = Category.objects.all()
   cakes = Cake.objects.all()
   return render(request,'master.html',{'categories':categories,'cakes':cakes})

def showCake(request,id):
   categories = Category.objects.all()
   cakes = Cake.objects.filter(category = id)
   return render(request,'master.html',{'categories':categories,'cakes':cakes})

def viewDetails(request,id):
   categories = Category.objects.all()
   cakes = Cake.objects.filter(id = id)
   return render(request,'viewdetails.html',{'categories':categories,'cakes':cakes})

def signup(request):
   if request.method == 'POST':
      uname = request.POST['username']
      password = request.POST['password']
      try:
         user = UserMaster.objects.get(username=uname)
         messages.error(request,'User already exists',extra_tags='danger')
         return redirect(signup)
      except:
         u1 = UserMaster(uname,password)
         u1.save()
         messages.error(request,'User created Successfully',extra_tags='success')
         return redirect(signup)
         
   categories = Category.objects.all()
   return render(request,'signup.html',{'categories':categories})

def login(request):
   if request.method == 'POST':
      uname = request.POST['username']
      password = request.POST['password']
      try:
         user = UserMaster.objects.get(username=uname,password=password)
         request.session["uname"] = uname 
         return redirect(home)
      except:
         messages.error(request,'Invalid Username Password',extra_tags='danger')
         return redirect(login)
   categories = Category.objects.all()
   return render(request,'login.html',{'categories':categories})

def logout(request):
   del request.session["uname"]
   return redirect(home)

def addtocart(request):
   if request.method == 'POST':
      if "uname" in request.session:
         cake_id = request.POST['cake_id']
         qty = request.POST['quantity']
         cake = Cake.objects.get(id = request.POST['cake_id'])
         user = UserMaster.objects.get(username=request.session['uname'])
         
         c1 = MyCart()
         c1.cake = cake
         c1.user = user
         c1.qty = qty
         c1.save()
         return redirect(home)
      else:
         messages.error(request,'Please Login to add item in cart !!!',extra_tags='danger')
         return redirect(login)
      

def showcart(request):
   if "uname" in request.session:
      user = UserMaster.objects.get(username=request.session['uname'])
      mycart = MyCart.objects.filter(user=user)
      categories = Category.objects.all()
      total=0
      for cart in mycart:
        total+=cart.cake.price*cart.qty
      return render(request,'cart.html',{'categories':categories,'cart':mycart,'total':total})
   else:
      messages.error(request,'Please Login to see cart items !!!',extra_tags='danger')
      return redirect(login)