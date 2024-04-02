from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductFormSerializer

# Create your views here.

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFormSerializer

    def perform_create(self,serializer):
        print(serializer.validated_data)
        #serializer.save()
        title = serializer.validated_data('title')
        content = serializer.validated_data('content')

        if content in None:
            content = title
        serializer.save()

        #send django signal



product_List_create_view = ProductListCreateApiView.as_view()

class ProductCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFormSerializer

    def perform_create(self,serializer):
        print(serializer.validated_data)
        #serializer.save()
        title = serializer.validated_data('title')
        content = serializer.validated_data('content')

        if content in None:
            content = title
        serializer.save()

        #send django signal



product_create_view = ProductCreateApiView.as_view()

class ProductCreateApiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFormSerializer

    def perform_create(self,serializer):
        print(serializer.validated_data)
        #serializer.save()
        title = serializer.validated_data('title')
        content = serializer.validated_data('content')

        if content in None:
            content = title
        serializer.save()

        #send django signal



product_create_view = ProductCreateApiView.as_view()

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFormSerializer

product_detail_view = ProductDetailApiView.as_view()

# class ProductListApiView(generics.RetrieveAPIView):
#    queryset = Product.objects.all()
#    serializer_class = ProductFormSerializer
     

# product_list_view =  ProductListApiView.as_view()