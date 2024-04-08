from rest_framework import routers
from products.viewsets import ProductViewSet

router = routers.DefaultRouter()
router.register('products-abc',ProductViewSet,basename='products')

urlpatterns = router.urls