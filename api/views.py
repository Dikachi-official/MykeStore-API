from django.shortcuts import render
from . models import *
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ProductsViewSet(ModelViewSet):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer


