from django.urls import path 
from .views import index,product_detail,add_to_cart,cart_view,remove_from_cart,search_product
urlpatterns = [
    path('index',index,name="index"),
    path('product-detail/<int:id>',product_detail,name='product-detail'),
    path('add-to-cart/<int:id>/',add_to_cart,name="add-to-cart"),
    path('cart',cart_view,name="cart-view"),
    path('remove/<int:id>',remove_from_cart,name="remove-from-cart"),
    path('search/',search_product,name="search_query"),
    
]

