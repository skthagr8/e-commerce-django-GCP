from django.shortcuts import render
from .models import Product, Category, SubCategory
from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer