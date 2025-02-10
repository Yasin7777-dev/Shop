from django.db import models
from django.db import models
import hashlib

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.FloatField()
    category = models.CharField(max_length=100, default='Без катеории')
    color = models.CharField(max_length=50, default='Без цвет')
    sku = models.CharField(max_length=10,unique=True,blank=True)

    def generate_sku_dla_shop(self):
        sku_string = f"{self.name}-{self.category}-{self.color}"
        hashed = hashlib.md5(sku_string.encode('utf-8')).hexdigtest()
        return hashed[:10].upper() 
   
    def save(self,*args,**kwargs):
        if not self.sku:
            self.sku = self.generate_sku_dla_shop()
        if Product.objects.filter(sku=self.sku).exists():
            raise ValueError('Продукт с этим  ску уже сущ')
        super().save(*args,**kwargs)

   
   
    def __str__(self):
        return self.name
    


# Create your models here.
