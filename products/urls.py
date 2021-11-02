from django.urls import path
from .views import ProductsListView, ProductImagesView,MenProductsView,WomanProductsView

app_name = 'products'

urlpatterns = [
    path('products/', ProductsListView.as_view(), name='products_list'),
    path('product-images/<int:pk>/', ProductImagesView.as_view(), name='product_images'),
    path('men-products/', MenProductsView.as_view(), name='men_products'),
    path('women-products/', WomanProductsView.as_view(), name='women_products')
]