from django.urls import path 
from .views import update_quantity,place_order,user_order_list,payment_page,start_online_payment,payment_success,payment_failed
urlpatterns = [
    path('update_quantity',update_quantity,name="update-quantity"),
    path('place_order',place_order,name="place-order"),
    path('orders',user_order_list,name="orders"),
    path('payment',payment_page,name="payment-page"),
    path('start-online-payment/<int:order_id>/', start_online_payment, name='start-online-payment'),
    path('payment-success/', payment_success, name='payment-success'),
    path('payment-failed/', payment_failed, name='payment-failed'),


]
