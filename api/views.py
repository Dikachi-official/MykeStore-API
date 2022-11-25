from django.shortcuts import render
from . models import *
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

# Create your views here.
class APIProducts(ListCreateAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer


class APIProduct(RetrieveUpdateDestroyAPIView):
    queryset= Product.objects.all()
    serializer_class = ProductSerializer



