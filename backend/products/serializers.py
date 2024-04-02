from rest_framework import serializers

from .models import Product

class ProductFormSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Product
        fields = ['title' ,'content', 'price','disc_price','my_discount']
    
    def get_my_discount(self, obj): 
        return obj.get_discount()