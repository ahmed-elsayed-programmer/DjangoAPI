from rest_framework import  mixins,viewsets

from products.models import Product
from products.serializers import ProductSerializer

class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductGenericViewSet( 
  mixins.ListModelMixin ,
  mixins.RetrieveModelMixin
   ,viewsets.GenericViewSet):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer 
  lookup_field = 'pk'