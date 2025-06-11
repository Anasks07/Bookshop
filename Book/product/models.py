from django.db import models
from user.models import User
# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=70,unique=True)
    
    def __str__(self):
        return self.name 
    
class Book(models.Model):
    title = models.CharField(max_length=250)
    genre = models.ForeignKey(Genre,on_delete=models.CASCADE,related_name='books')
    price = models.DecimalField(max_digits=10,decimal_places=2)
    photo = models.ImageField(upload_to='book_pictures/',blank=True,null=True) 
    
    def __str__(self):
        return self.title

