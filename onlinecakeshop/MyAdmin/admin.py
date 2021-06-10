from django.contrib import admin
from MyAdmin.models import Category,Cake
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
   list_display = ['cname']

class CakeAdmin(admin.ModelAdmin):
   list_display = ['cakename','price','description','imageurl','category']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Cake,CakeAdmin)