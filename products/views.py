from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serizlizers import ProductsSerializer, ProductImagesSerializer


class ProductsListView(ListAPIView):

    queryset = Products

    def get(self, request, **kwargs):
        products = Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductImagesView(APIView):

    def get(self, request, pk):
        product = Products.objects.get(id=pk)
        images = ProductImages.objects.filter(product=product)
        serializer = ProductImagesSerializer(images, many=True)
        data = {
            'name': product.name,
            'description': product.description,
            'price': product.price,
            'discount': product.discount,
            'company': product.company.name,
            'images': serializer.data,

        }
        print(serializer.data)
        return Response(data=data, status=status.HTTP_200_OK)


class MenProductsView(APIView):

    def get(self, request):
        products = Products.objects.filter(gender='male').all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WomanProductsView(APIView):

    def get(self, request):
        products = Products.objects.filter(gender='female').all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)