from django.urls import path,include
from . import views
from .views import ProductViewSet, CategoryViewSet
from rest_framework import routers
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register('products',views.ProductViewSet)
router.register('categories', views.CategoryViewSet)
urlpatterns = router.urls


#urlpatterns = [
    #path('products/', views.APIProducts.as_view(), name = 'products'),
    #path('product/<str:pk>', views.APIProduct.as_view(), name = 'product')
#]