from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductFormSerializer
from django.shortcuts import get_object_or_404

class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFormSerializer

    def perform_create(self,serializer):
        print(serializer.validated_data)
        serializer.save()
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if content is None:
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

@api_view(['GET','POST'])
def product_alt_view(request,*args, **kwargs):
    method = request.method 

    if method == 'GET':
        pass
        # url arguments
        # get request -> detail view
        # list view
        query_set = Product.objects.all()


    if method == 'POST':
         
        #create an item

        serializer = ProductFormSerializer(data = request.data)

        if serializer.is_valdi(raise_exception=True):
            print(serializer.data)
            return Response(serializer.data)
        
        return Response({"invalid":"not a good data"})
    
    
     