from django.db import models
from user.models import User
from product.models import Book
# Create your models here.



class Order(models.Model):
    STATUS_CHOICES = [
        ('pending','Pending'),
        ('shipped','Shipped'),
        ('delivered','Delivered'),
        ('cancelled','Cancelled'),
    ]
    
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    total_price = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=10, choices=[('cod', 'Cash on Delivery'), ('online', 'Online Payment')],default='cod')
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    razorpay_signature = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return f"Order{self.id} - {self.user.username} - {self.status}"




class OrderedItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Book,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    
    def __str__(self):
        return f"{self.item.title} ({self.quantity}) - Order {self.order.id}"


def user_orders(self):
    return self.items.all()