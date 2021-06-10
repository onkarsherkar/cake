from django.shortcuts import render,HttpResponse

# Create your views here.

# Test link
def hello(request):
   return HttpResponse('Hello CakeShop')

