from rest_framework import  mixins, viewsets
from .models import Product
from .serializers import ProductFormSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductFormSerializer
    lookup_field = 'pk'

class ProductGenericViewSet(viewsets.ModelViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductFormSerializer
    lookup_field = 'pk'