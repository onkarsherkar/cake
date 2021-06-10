from django.db import models
from MyAdmin.models import Cake
# Create your models here.

class UserMaster(models.Model):
   username = models.CharField(max_length=20,primary_key=True)
   password = models.CharField(max_length=20)

   class Meta:
      db_table = 'UserMaster'

class MyCart(models.Model):
   cake = models.ForeignKey(Cake,on_delete=models.CASCADE)
   user = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
   qty = models.IntegerField()

   class Meta:
      db_table = 'Mycart'