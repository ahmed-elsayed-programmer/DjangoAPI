from rest_framework import generics , mixins , permissions , authentication

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsStaffEditorPermission

# Create your views here.

class ProductMixinView(mixins.ListModelMixin , mixins.RetrieveModelMixin, generics.GenericAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
  lookup_field = 'pk'

  def get(self , request , *args, **kwargs):
      pk = kwargs.get('pk')
      if pk is not None :
          return self.retrieve(request , *args, **kwargs)
      
      return self.list(request , *args, **kwargs)
class ProductCreateApiView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]

    def perform_create(self, serializer:ProductSerializer):
        instance = serializer.save() 
        if not instance.content :
            instance.content = instance.title 

class ProductDetailsApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]


class ProductDestroyApiView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]

    lookup_field = 'pk'
class ProductUpdatesApiView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [IsStaffEditorPermission]


    def perform_update(self, serializer):
        instance = serializer.save() 

        if not instance.content :
            instance.content = instance.title 
            instance.save()