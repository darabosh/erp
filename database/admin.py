from django.contrib import admin
from database.models import *

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Facility)
admin.site.register(FacilityInventory)
admin.site.register(InventoryItem)
admin.site.register(Order)
admin.site.register(OrderItem)
