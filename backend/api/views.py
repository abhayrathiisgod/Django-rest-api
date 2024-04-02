from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

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

