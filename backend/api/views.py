import json
from django.forms.models import model_to_dict
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response


from products.models import Product
from products.serializers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def api_home(request , *args, **kwargs):
    instance = Product.objects.all().order_by('?').last()
    data = {}
    if instance:
        data = ProductSerializer(instance).data

    return Response(data)