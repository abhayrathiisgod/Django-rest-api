from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductFormSerializer


class ProductViewSet(viewsets.ModelViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View
    post -> create -> New Instance
    put -> Update
    patch -> Partial UPdate
    delete -> destroy 
    '''
    queryset = Product.objects.all()
    serializer_class = ProductFormSerializer
    lookup_field = 'pk'  # default


class ProductGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet):
    '''
    get -> list -> Queryset
    get -> retrieve -> Product Instance Detail View 
    '''
    queryset = Product.objects.all()
    serializer_class = ProductFormSerializer
    lookup_field = 'pk'  # default
