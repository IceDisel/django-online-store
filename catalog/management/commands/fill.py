import json

from django.core.management.base import BaseCommand
from catalog.models import Category, Product
from django.db import connection


def reset_sequence(model):
    with connection.cursor() as cursor:
        cursor.execute(
            f"SELECT setval(pg_get_serial_sequence('{model._meta.db_table}', 'id'), "
            f"coalesce(max(id), 1), max(id) IS NOT null) FROM {model._meta.db_table};")


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open('catalog_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        categories = {}
        for item in data:
            if item['model'] == 'catalog.category':
                categories[item['pk']] = item['fields']
        return categories

    @staticmethod
    def json_read_products():
        with open('catalog_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        products = {}
        for item in data:
            if item['model'] == 'catalog.product':
                products[item['pk']] = item['fields']
        return products

    def handle(self, *args, **options):

        Product.objects.all().delete()
        reset_sequence(Product)

        Category.objects.all().delete()
        reset_sequence(Category)

        product_for_create = []
        category_for_create = []

        for pk, fields in Command.json_read_categories().items():
            category_for_create.append(
                Category(name=fields['name'], description=fields['description'])
            )

        Category.objects.bulk_create(category_for_create)

        for pk, fields in Command.json_read_products().items():
            product_for_create.append(
                Product(name=fields['name'], description=fields['description'],
                        image=fields['image'], category=Category.objects.get(pk=fields['category']),
                        price=fields['price'], created_at=fields['created_at'],
                        updated_at=fields['updated_at'])
            )

        Product.objects.bulk_create(product_for_create)

        print("Загрузка данных в БД выполнена")
