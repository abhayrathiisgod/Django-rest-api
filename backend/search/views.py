from rest_framework import generics
# from rest_framework import request
from rest_framework.response import Response
from products.models import Product, ProductManager
from products.serializers import ProductFormSerializer
# Create your views here.

from . import client


class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        tag = request.GET.get('tag') or None
        if not query:
            return Response('', status=400)
        result = client.perform_search(query, tags=[tag])
        return Response(result)


class SearchListoldview(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductFormSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        query = self.request.GET.get('q')
        user = None
        results = Product.objects.none()

        if query is not None:
            if self.request.user.is_authenticated:
                user = self.request.user
            results = qs.search(query, user=user)

            return results

        return results
