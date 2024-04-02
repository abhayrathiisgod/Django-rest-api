from django.shortcuts import render
from django.forms.models import model_to_dict
#from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
import json
from products.models import Product
from products.serializers import ProductFormSerializer
from rest_framework.decorators import api_view

# Create your views here.
'''
def api_home(request, *args, **kwargs):
    
     # request -> http request -> Django
    # json data -> request.body 
    # request.body

    print(request.GET) # gets the url params
    print(request.POST)
    body = request.body
    print(body)

    # to convert the given string to actual python dictionary
    data = {}

    try:
        data = json.loads(body)
    except:
        pass
    #print(data.keys())
    print(data)
    # data['headers'] = request.headers
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type

    print(request.headers)
    #return JsonResponse({"message":"Jango api response message"})

    return JsonResponse(data)
    
    #model_data = Product.objects.all().order_by("?").first()
    #data = {}

   # if model_data:
        
        data['id'] = model_data.id  # ofc by default
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price

        #data = model_to_dict(model_data, fields=['contetn','price'])

        # in above model_data -> convert to python dictionary -> then return as json
        #json_data_str = json.dumps(data)
    
    #return JsonResponse(data) 
'''
# using drf
#@api_view(['GET','POST'])
#def api_home(request,*args,**kwargs):
  
    #DRF API VIEW


    #if request.method == 'GET':
        #return Response({"WARNING: GET METHOD NOT ALLOWED"}, status=405)
    
    
    #instance = Product.objects.all().order_by("?").first()

    # gotta store  in dict

    #data = {}

    #if instance:
        #data = ProductFormSerializer(instance).data

    #return Response(data)

@api_view(['GET','POST'])
def api_home(request, *args,**kwargs):
    serializers = ProductFormSerializer(data=request.data)

    if serializers.is_valid(raise_exception=True) == True:
        serializers.save()
        data = serializers.data
        print(serializers.data)
        return Response(data)

    return Response({"WARNING":"NOT GOOD DATA"})
