from django.shortcuts import render,redirect,get_object_or_404
from .models import Genre,Book
from django.contrib import messages 
from user.models import Cart
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.
def index(request):
    product = Book.objects.all()
    
    return render(request,'index.html',{'product':product})

def create_product(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        price = request.POST.get('price')
        image = request.FILES.get('image')
        
        if not title:
            message_status = "Please provide title"
            messages.error(request,message_status)
            return render(request,'addproduct.html')
            
        if not genre:
            message_status = "Please provide genre"
            messages.error(request,message_status)
            return render(request,'addproduct.html')
       
        if not price:
            message_status = "Please provide price"
            messages.error(request,message_status)
            return render(request,'addproduct.html')
        
        if not image:
            message_status = "Please provide image"
            messages.error(request,message_status)
            return render(request,'addproduct.html')
            
            
        
        product = Book.objects.create(title=title, genre=genre, price=price, image=image)
        product.save()
        return redirect('index')
    
    return render(request,'addproduct.html')



def update_product(request,id):
    product = Book.objects.get(id=id)

    if request.method == 'POST':
        title = request.POST.get('title')
        genre = request.POST.get('genre')
        price = request.POST.get('price')
        image = request.FILES.get('image') 
        
        
        if title:
            product.title = title 
        
        if genre:
            product.genre = genre 
        
        if price:
            product.price = price 
        
        if image:
            product.image = image
        
        product.save()
        return redirect('/')
    
    context={
        'data':product
    }
        
    return render(request,'addproduct.html',context)


def add_to_cart(request, id):
    book_obj = get_object_or_404(Book, id=id)
    user = request.user
    
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        book_obj = get_object_or_404(Book, id=id)
        user = request.user

        if Cart.objects.filter(item=book_obj, user=user).exists():
            return JsonResponse({'status': 'info', 'message': 'This item is already in the cart.'})

        Cart.objects.create(item=book_obj, user=user)
        return JsonResponse({'status': 'success', 'message': 'Added to cart.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)
    
   
def remove_from_cart(request,id):
    cart_item = get_object_or_404(Cart,id=id)
    cart_item.delete()
    return redirect('cart-view')

def product_detail(request,id):
    book_obj = get_object_or_404(Book,id=id)
    context={
        'book_obj':book_obj
    }
    return render(request,'productdetail.html',context)  

def cart_view(request):
    user = request.user 
    cart_obj = Cart.objects.filter(user = user)
    context = {
        'cart_obj':cart_obj
    }
    return render(request,'cart.html',context)

def remove_product(request,id):
    product = Book.objects.get(id=id)
    product.delete()
    return redirect('/')


def search_product(request):
    if request.method=='GET':
        search_query = request.GET.get('q', '') 
       
        
        if search_query:
            product = Book.objects.filter(Q(title__icontains=search_query)|Q(genre__name__icontains=search_query)) 
            context={
                'product':product
            }
            return render(request,'search_page.html',context)
        
        return redirect('index')




# def add_to_cart(request,id):
#     book_obj = get_object_or_404(Book,id=id)
#     user = request.user 
    
#     if Cart.objects.filter(item = book_obj, user = user).exists():
#         messages.info(request,'This item is already in the cart.')
#         return redirect('product-detail',id=book_obj.id)
    
    
#     Cart.objects.create(item = book_obj, user = user)
#     messages.success(request,'Added to cart.')
#     return redirect('index')