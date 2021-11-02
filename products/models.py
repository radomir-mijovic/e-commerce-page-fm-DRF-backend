from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    image = models.ImageField(upload_to='media/profile_image', null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductImages(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='images')
    images = models.ImageField(upload_to='media/images', null=True, blank=True)

    def __str__(self):
        return str(self.product.name)
