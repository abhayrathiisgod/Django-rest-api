from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=50,blank= False, default="Enter Your title")
    content = models.CharField(max_length=50,blank=True, null=False , default = "enter your content")
    price = models.DecimalField(max_digits = 8, decimal_places = 4, default= 99.9999)

    def __str__(self) -> str:
        return self.title
    
    @property
    def disc_price(self):
        return "%.2f" %(float(self.price)*0.8)
    
    def get_discount(self):
        return "122"