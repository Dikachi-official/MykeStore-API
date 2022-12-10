from django.shortcuts import render
from . models import *
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer, CartSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .filter import ProductFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet



# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['names','description']
    ordering_fields = ['price']
    pagination_class = PageNumberPagination



class CategoryViewSet(ModelViewSet):
    queryset= Category.objects.all()
    serializer_class = CategorySerializer



class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer   

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {"product_id":self.kwargs["product_pk"]}     



class CartViewSet(CreateModelMixin,RetrieveModelMixin,GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
