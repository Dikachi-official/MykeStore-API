from django.shortcuts import render
from . models import *
from .serializers import ProductSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .filter import ProductFilter
from rest_framework.filters import SearchFilter

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter


class CategoryViewSet(ModelViewSet):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer


