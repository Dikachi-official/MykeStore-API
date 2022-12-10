from django.db import models
from django.contrib.auth.models import User
import uuid  # TO USE UUID
from django.conf import settings


# Create your models here.


# PRODUCTS
# FOR PRODUCTS AND GADGETS CATEGORY
class Category(models.Model):
    title = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          primary_key=True, unique=True)
    slug = models.SlugField(default=None, null=True, blank =True)
    featured_products = models.OneToOneField(
        'Product', on_delete=models.CASCADE, blank=True, null=True, related_name='featured_product')
    icon = models.CharField(
        max_length=100, default=None, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False,
                          primary_key=True, unique=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='products')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(
        upload_to='img', blank=True, null=True, default='')
    slug = models.SlugField(default=None, null=True, blank=True)
    inventory = models.IntegerField(default=5)

    def __str__(self):
        return self.name  # TO IDENTIFY CLASS BY NAME


class Review(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="reviews")
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to='img', default=" ", null=True, blank=True)


class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name="items", null=True, blank=True)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='cartitems', blank=True, null=True)
    quantity = models.PositiveSmallIntegerField(default=0)
