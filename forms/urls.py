from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('order/create/', views.order_create, name='order_create'),
    path('product/add/', views.product_form, name='add_product'),
    path('product/edit/<int:product_id>/', views.product_form, name='edit_product'),
    path('category/add/', views.category_form, name='add_category'),
    path('category/edit/<int:category_id>/', views.category_form, name='edit_category'),
    path('facility/add/', views.facility_form, name='add_facility'),
    path('facility/edit/<int:facility_id>/', views.facility_form, name='edit_facility'),
    path('product/list/', views.product_list, name='product_list'),
    path('category/list/', views.category_list, name='category_list'),
    path('facility/list/', views.facility_list, name='facility_list'),
]