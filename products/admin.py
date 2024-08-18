from django.contrib import admin

from products.models import Product, Order, OrderProduct

# Register your models here.
admin.site.register(Product)
admin.site.register(OrderProduct)

class OrderProductInline(admin.TabularInline):
    model = OrderProduct
    extra = 1

    fields = ('product', 'quantity',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderProductInline]

    fields = ('user',)
    readonly_fields = ('total_price',)