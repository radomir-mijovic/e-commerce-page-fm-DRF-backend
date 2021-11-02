from rest_framework import serializers
from .models import *


class ProductsSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    company = serializers.SlugRelatedField(read_only=True, slug_field='name')

    class Meta:
        model = Products
        fields = ['id', 'name', 'image', 'price', 'discount', 'company', 'gender']


class ProductImagesSerializer(serializers.ModelSerializer):
    images = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = ProductImages
        fields = ['images']

