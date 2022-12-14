from django.urls import path,include
from . import views
from .views import ProductViewSet, CategoryViewSet, CartViewSet, ReviewViewSet
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter


router = routers.DefaultRouter

router = DefaultRouter()
# PRODUCT PARENT ROUTER
# localhost:8000/api/products/product_id/reviews/
router.register('products', views.ProductViewSet)  # PRODUCT PARENT ROUTER
product_router = routers.NestedDefaultRouter(router, 'products', lookup="product")
product_router.register('reviews', views.ReviewViewSet, basename="product-reviews")# Register our (line 13) variable


# CART PARENT ROUTER
router.register('carts', views.CartViewSet)  
cart_router = routers.NestedDefaultRouter(router, 'carts', lookup="cart")
cart_router.register("items", views.CartItemViewSet, basename = "cart-items")



urlpatterns = [
    # URL ENDPOINT:localhost/api/product/product-uuid
    path('', include(router.urls)),

    # URL ENDPOINT:localhost/api/products/product-uuid/reviews
    path('', include(product_router.urls)),

    #URL ENDPOINT:localhost/api/carts/cart-uuid/items
    path('', include(cart_router.urls))
]    

#urlpatterns = [
    #path('products/', views.APIProducts.as_view(), name = 'products'),
    #path('product/<str:pk>', views.APIProduct.as_view(), name = 'product')
#]