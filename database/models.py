from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Facility(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FacilityInventory(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='InventoryItem')
    inventory_date = models.DateField(auto_now=True)
    timestamp = models.DateTimeField(auto_now=True)

class InventoryItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    facility_inventory = models.ForeignKey(FacilityInventory, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    STATUS_CHOICES = [("naruceno","naruceno"), ("poslato","poslato"), ("stiglo","stiglo")]
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)
    order_date = models.DateField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_CHOICES[0][0])
    timestamp = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField(Product, through='OrderItem')
    total = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    @property
    def calculate_subtotal(self):
        return self.product.price * self.quantity

    def save(self, *args, **kwargs):
        self.subtotal = self.calculate_subtotal
        super().save(*args, **kwargs)