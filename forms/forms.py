from django import forms
from database.models import Product, Category, Facility, FacilityInventory, Order, OrderItem


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class FacilityForm(forms.ModelForm):
    class Meta:
        model = Facility
        fields = '__all__'

class FacilityInventoryForm(forms.ModelForm):
    class Meta:
        model = FacilityInventory
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = '__all__'