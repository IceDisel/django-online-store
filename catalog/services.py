from django.core.cache import cache

from catalog.models import Category, Product
from config.settings import CACHE_ENABLED


def get_categories_from_cache():
    if not CACHE_ENABLED:
        return Category.objects.all()

    key = 'categories'
    cache_data = cache.get(key)

    if cache_data is not None:
        return cache_data

    cache_data = Category.objects.all()
    cache.set(key, cache_data)

    return cache_data


def get_category_products_from_cache(pk):
    if not CACHE_ENABLED:
        return Product.objects.filter(category=pk)

    key = 'category_products'
    cache_data = cache.get(key)

    if cache_data is not None:
        return cache_data

    cache_data = Product.objects.filter(category=pk)
    cache.set(key, cache_data)

    return cache_data
