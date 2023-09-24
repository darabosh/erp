from django.shortcuts import render, redirect
from database.models import Product, Category, Facility, FacilityInventory, Order, OrderItem
from .forms import ProductForm, CategoryForm, FacilityForm, FacilityInventoryForm, OrderForm, OrderItemForm

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def order_create(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        order_item_form = OrderItemForm(request.POST)

        if order_form.is_valid() and order_item_form.is_valid():
            # Process form data and create order
            # You can also handle form submissions here
            pass
    else:
        order_form = OrderForm()
        order_item_form = OrderItemForm()

    return render(
        request,
        'order_create.html',
        {'order_form': order_form, 'order_item_form': order_item_form},
    )

def product_form(request, product_id=None):
    if product_id:
        product = Product.objects.get(pk=product_id)
    else:
        product = None

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to product list after successful form submission
    else:
        form = ProductForm(instance=product)

    return render(request, 'product_form.html', {'form': form, 'product': product})

# View for adding/editing a category
def category_form(request, category_id=None):
    if category_id:
        category = Category.objects.get(pk=category_id)
    else:
        category = None

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')  # Redirect to category list after successful form submission
    else:
        form = CategoryForm(instance=category)

    return render(request, 'category_form.html', {'form': form, 'category': category})

# View for adding/editing a customer
def facility_form(request, facility_id=None):
    if facility_id:
        facility = Facility.objects.get(pk=facility_id)
    else:
        facility = None

    if request.method == 'POST':
        form = FacilityForm(request.POST, instance=facility)
        if form.is_valid():
            form.save()
            return redirect('facility_list')  # Redirect to customer list after successful form submission
    else:
        form = FacilityForm(instance=facility)

    return render(request, 'facility_form.html', {'form': form, 'facility': facility})

def category_list(request):
    # Retrieve a list of all categories from the database
    categories = Category.objects.all()

    # You can perform additional logic here if needed

    # Render the 'category_list.html' template with the list of categories
    return render(request, 'category_list.html', {'categories': categories})

def facility_list(request):
    # Retrieve a list of all customers from the database
    facilitys = Facility.objects.all()

    # You can perform additional logic here if needed

    # Render the 'customer_list.html' template with the list of customers
    return render(request, 'facility_list.html', {'facilitys': facilitys})

def product_list(request):
    # Retrieve a list of all products from the database
    products = Product.objects.all()

    # You can perform additional logic here if needed

    # Render the 'product_list.html' template with the list of products
    return render(request, 'product_list.html', {'products': products})