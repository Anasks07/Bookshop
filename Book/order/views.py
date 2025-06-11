from django.shortcuts import render,redirect
from user.models import Cart
from.models import Order,OrderedItem,user_orders
import razorpay 
from django.conf import settings 
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def update_quantity(request):
    if request.method == "POST":
        cart_item_id = request.POST.get('cart_item_id')
        quantity = int(request.POST.get('quantity',1))
        
        cart_item = Cart.objects.get(id=cart_item_id)
        cart_item.quantity = quantity
        cart_item.save()
        return redirect('cart-view')




def payment_page(request):
    cart_item_id = request.GET.get('cart_item_id')
    quantity = int(request.GET.get('quantity',1))
    total_price = float(request.GET.get('total_price'))
    
    context = {
        'cart_item_id':cart_item_id,
        'quantity':quantity,
        'total_price':total_price
    }
    return render(request,'paymentpage.html',context)




def place_order(request):
    if request.method == 'POST':
        cart_item_id = request.POST.get('cart_item_id')
        quantity = int(request.POST.get('quantity'))
        total_price = float(request.POST.get('total_price'))
        payment_method = request.POST.get('payment_method')
        
        cart_item = Cart.objects.get(id=cart_item_id)
        cart_item.quantity = quantity
        cart_item.save()
        
        
        # total_price = cart_item.item.price * quantity 
        order = Order.objects.create(user = request.user,total_price = total_price,payment_method=payment_method)
        OrderedItem.objects.create(order=order,item = cart_item.item,quantity=quantity,price = total_price)
        
        cart_item.delete()
        
        if payment_method == 'online':
            return redirect('start-online-payment',order_id=order.id)
        else:
            return redirect('orders')



@csrf_exempt
def start_online_payment(request,order_id):
    order = Order.objects.get(id=order_id)
    
    client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID,settings.RAZORPAY_KEY_SECRET))
    
    razorpay_order = client.order.create({
        "amount": int(order.total_price * 100),
        "currency": "INR",
        "payment_capture":"1"
    })
    
    order.razorpay_order_id = razorpay_order['id']
    order.save()
    
    context = {
        "order" : order,
        "razorpay_key": settings.RAZORPAY_KEY_ID,
        "razorpay_order_id": razorpay_order['id'],
        "amount": int(order.total_price * 100),
        "currency": "INR"
    }
    return render(request,"online_payment.html",context)


@csrf_exempt
def payment_success(request):
    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        payment_id = request.POST.get('razorpay_payment_id')
        razorpay_order_id = request.POST.get('razorpay_order_id')
        signature = request.POST.get('razorpay_signature')

        order = Order.objects.get(id=order_id)
        order.razorpay_payment_id = payment_id
        order.razorpay_order_id = razorpay_order_id
        order.razorpay_signature = signature
        order.save()

        return render(request, 'payment_success.html', {'order': order})
   

def payment_failed(request):
    return render(request, "payment_failed.html")






def user_order_list(request):
    user = request.user 
    orders = Order.objects.filter(user = user).prefetch_related('items__item').order_by('-created_at')
    
  
    return render(request,'order.html',{'orders':orders})



# def place_order(request): 
#     user = request.user 
#     cart_item = Cart.objects.filter(user = user)
    
#     if not cart_item.exists():
#         return redirect('cart-view')
    
#     total = sum(item.item.price * item.quantity for item in cart_item)
    
#     order = Order.objects.create(user = user, total_price = total)
    
#     for item in cart_item:
#         OrderedItem.objects.create(order = order,item = item.item, quantity = item.quantity,price = item.item.price)
    
#     return redirect('cart-view')





