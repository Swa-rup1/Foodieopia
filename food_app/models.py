from django.db import models
from django.contrib.auth.models import User






class Person(models.Model):
    first_name = models.CharField (max_length=50,null=False,default='first')
    lastName = models.CharField(max_length=30,null=False,default="last")
    username =  models.CharField(max_length=30,null=False,default="user")
    password = models.CharField(max_length=40)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.first_name+ self.lastName
    

class Collection(models.Model):
    collection_name = models.CharField(max_length=100,null=False)
    collection_price = models.IntegerField(null=False)
    collection_image = models.ImageField(null=False,upload_to='media/pooja_app/images/collections/')
    def __str__(self):
        return self.collection_name
    
    
class Item (models.Model):
    item_name = models.CharField(max_length=300)
    item_price = models.IntegerField()
    item_image  = models.ImageField(null=False, upload_to='media/pooja_app/images/items/')
    category_id = models.ForeignKey(Collection,on_delete=models.SET_NULL,null=True)
    
    def __str__(self):
        return self.item_name
    
class Cart(models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.SET_NULL,null=True)
    person_id = models.IntegerField(null=True)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('Item', through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey('Item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    item_price = models.DecimalField(max_digits=10, decimal_places=2)


