from django.shortcuts import render
from .models import Product, Category, SubCategory
from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer, SubCategorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def get_queryset(self):
        queryset = super().get_queryset()
        category_name = self.request.query_params.get('category', None)
        product_title = self.request.query_params.get('product_title', None)

        if category_name is not None:
            queryset = queryset.filter(category__name=category_name)
        if product_title is not None:
            queryset = queryset.filter(product_title__iexact=product_title)

        return queryset


    @action(detail=False, methods=['get'], url_path='by-category/(?P<category_name>[^/.]+)')
    def by_category(self, request, category_name=None):
        products = Product.objects.filter(category__name=category_name)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    

    @action(detail=False, methods=['get'], url_path='by-product-title/(?P<product_title>[^/.]+)')
    def by_product_title(self, request, product_title=None):
        products = Product.objects.filter(title__iexact=product_title)
        serializer = self.get_serializer(products, many=True)
        return Response(serializer.data)
    



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer