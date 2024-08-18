from django.db import models, transaction
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    is_18_plus = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    total_price = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    products = models.ManyToManyField(Product, through="OrderProduct")

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=2)

@receiver(post_save, sender=Order)
def update_order_total_price(sender, instance, **kwargs):
    with transaction.atomic():
        order = instance.order
        order.total_price = sum([op.price for op in order.orderproduct_set.all()])
        order.save()

@receiver(pre_save, sender=OrderProduct)
def update_order_product_price(sender, instance, **kwargs):
    instance.price = instance.price * instance.quantity