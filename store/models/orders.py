from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Shipped','Shipped'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
        ('Canceled','Canceled')
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address1 = models.CharField(max_length=50, default='', blank=True)
    address2 = models.CharField(max_length=50, default='', blank=True)
    pincode = models.CharField(max_length=7, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status=models.CharField(max_length=50,null=True,choices=STATUS)

    def placeOrder(self):
        self.save()
    
    def __str__(self):
        return self.customer.first_name +" "+ self.customer.last_name

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

