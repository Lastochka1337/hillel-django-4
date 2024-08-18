from django.db import models, transaction
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from products.models import Product


class Store(models.Model):
    name = models.CharField(max_length=100)
    products = models.ManyToManyField(Product, through="Inventory")

    def __str__(self):
        return self.name

class Inventory(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)

@receiver(pre_save, sender=Inventory)
def update_order_product_price(sender, instance, **kwargs):
    instance.price = instance.product.price * instance.quantity