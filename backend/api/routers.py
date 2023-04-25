from rest_framework.routers import DefaultRouter

from .viewsets import ProductViewSets , ProductGenericViewSet

router = DefaultRouter()

router.register('products' , ProductGenericViewSet , basename='products')

urlpatterns = router.urls