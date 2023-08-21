from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)        
    
    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)        
    
    def retrieve(self, request, pk=None):
        pass
    
    def update(self, request, pk=None):
        pass
    
    def destroy(self, request, pk=None):
        pass
    
      