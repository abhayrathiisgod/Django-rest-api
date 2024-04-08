from rest_framework import routers
from products.viewsets import ProductGenericViewSets

router = routers.DefaultRouter()
router.register('products-abc',ProductGenericViewSets,basename='products')

urlpatterns = router.urls