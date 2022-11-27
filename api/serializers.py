from . models import *
from . views import *
from rest_framework import serializers




class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'name', 'price', 'description', 'inventory'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'title', 'featured_products'
        )
