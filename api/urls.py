from django.urls import path,include
from . import views
from .views import ProductsViewSet, CategoryViewSet
from rest_framework.routers import DefaultRouter




router = DefaultRouter()
router.register('products',views.ProductsViewSet)
router.register('categories', views.CategoryViewSet)
urlpatterns = router.urls


urlpatterns = [
    #path('products/', views.APIProducts.as_view(), name = 'products'),
    #path('product/<str:pk>', views.APIProduct.as_view(), name = 'product')
]