from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=0)
    stock_quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Facility(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)

class FacilityInventory(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    last_updated = models.DateTimeField(auto_now=True)


class Order(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)