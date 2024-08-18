from django.contrib import admin

from orders.models import OrderProduct, Order
from products.models import Tag, Product, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(OrderProduct)
admin.site.register(Category)
admin.site.register(Tag)

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

    fields = ('product', 'quantity', 'price')
    readonly_fields = ('price',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]

    list_display = ('id', 'user', 'total_price', 'created_at')

    fields = ('user', 'total_price')
    readonly_fields = ('total_price',)