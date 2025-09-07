from rest_framework import serializers
from .models import Product, Category, SubCategory

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    category = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )

    sub_category = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True,
    )
    usage_id = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    gender_id = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    product_type_id = serializers.SlugRelatedField(
        slug_field='name',
        read_only=True
    )
    
        



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'