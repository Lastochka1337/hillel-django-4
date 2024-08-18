import random

from django.core.management import BaseCommand
from django.db import transaction

from products.models import Category, Product, Tag


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        categories =  ['Electronics', 'Clothing', 'Books', 'Drinks', 'Food']

        for category in categories:
            Category.objects.create(name=category)

        products_names = ['Coca-Cola', 'Fanta', 'Sprite', 'Mirinda', 'Pepsi']

        products = []
        for product_name in products_names:
            category = Category.objects.get(name='Food')
            price = random.randint(1, 100)

            products.append(category.products.create(name=product_name, price=price))

        tags_names = ["Top", "Best", "Cheap", "Expensive", "New", "Sale"]

        tags = [
            Tag(name=tag_name)
            for tag_name in tags_names
        ]

        Tag.objects.bulk_create(tags)

        for product in products:
            random_tags = random.choice(tags)

            product.tags.add(random_tags)
            product.save()