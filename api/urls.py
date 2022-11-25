from django.urls import path,include
from . import views
from .views import APIProduct,APIProducts


urlpatterns = [
    path('products/', views.APIProducts.as_view(), name = 'products'),
    path('product/<str:pk>', views.APIProduct.as_view(), name = 'product')
]