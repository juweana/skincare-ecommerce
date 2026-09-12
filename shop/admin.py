from django.contrib import admin
from .models import Category, Product, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {"slug":("name",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=["name","category","price","is_active"]
    list_filter =["category","is_active"]
    search_fields =["name"]
    list_editable = ["price", "is_active"]

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ["product", "quantity", "price"]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=["customer_name", "phone", "created_at"]
    search_fields = ["customer_name", "phone"]
    list_filter = ["created_at"]
    inlines = [OrderItemInline]

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order","product","quantity","price"]
    



