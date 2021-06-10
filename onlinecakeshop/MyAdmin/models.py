from django.db import models

# Create your models here.

class Category(models.Model):
   cname = models.CharField(max_length=50)

   def __str__(self):
      return self.cname

   class Meta:
      db_table = 'Category'

class Cake(models.Model):
   cakename = models.CharField(max_length=50)
   price = models.FloatField(default=1000)
   description = models.CharField(max_length=100)
   imageurl = models.ImageField(upload_to='images/',default='abc.jpg')
   category = models.ForeignKey(Category,on_delete=models.CASCADE)

   class Meta:
      db_table = 'Cake'