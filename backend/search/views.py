from rest_framework import generics
from rest_framework import request
from products.models import Product, ProductManager
from products.serializers import ProductFormSerializer
# Create your views here.


class SearchListview(generics.ListAPIView):
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
