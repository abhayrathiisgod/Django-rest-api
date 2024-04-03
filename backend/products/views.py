from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductFormSerializer
from django.shortcuts import get_object_or_404


#                       class based generic views 
#
#
#
#
#
#
#
#
class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFormSerializer

    def perform_create(self,serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')

        if content is None:
            content = title
        serializer.save()

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

product_create_view = ProductCreateApiView.as_view()

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFormSerializer

product_detail_view = ProductDetailApiView.as_view()

class ProductUpdateApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFormSerializer

    def perform_update(self, serializer):
        instance = serializer.save()

        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateApiView.as_view()


class ProductDestroyApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFormSerializer
    lookup_field = 'pk'

    def perform_destroy(self,instance):
        super().perform_destroy(instance)
        
product_destroy_view = ProductDestroyApiView.as_view()

#                   Function based Views
#
#
#
#
#
#
# using function based views to create retrieve list
@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*args, **kwargs):

    if request.method == 'GET':
        if pk is not None:
            # get detail view
            #query_set = Product.objects.filter(pk=pk)
            #if not query_set.exists():
                # or raise HTTP404
                #return Response({"error":"does not exist"}, status=400)
            #else:
                #data = ProductFormSerializer(query_set,many=False).data
                #return Response(data)
            
            obj = get_object_or_404(Product,pk=pk)
            data = ProductFormSerializer(obj, many= False).data
            return Response(data)     
        else:
            # list view
            query_set = Product.objects.all()
            data = ProductFormSerializer(query_set, many=True).data

        return Response(data)


    if request.method == 'POST':
         
        #create an item

        serializer = ProductFormSerializer(data = request.data)

        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')

            if content is None:
                content = title 
            serializer.save()
            print(serializer.data)
            return Response(serializer.data)
        
        return Response({"invalid":"not a good data"}, status=400)
    
    
    
     