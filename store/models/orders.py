from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    product = models.ManyToManyField(Product,blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=50, default='', blank=True)
    email = models.EmailField(max_length=50, default='', blank=True)
    price = models.IntegerField(default=0)
    address = models.CharField(max_length=500, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

