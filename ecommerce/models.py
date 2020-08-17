from django.db import models

# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=30)

class Products(models.Model):
    product_name = models.CharField(max_length=30)
    product_description = models.CharField(max_length=30)
    product_price = models.IntegerField()

class Pedidos(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    get_it = models.BooleanField()


