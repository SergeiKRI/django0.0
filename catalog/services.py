from catalog.models import Products
from config.settings import CACHE_ENABLED
from django.core.cache import cache


def get_products_from_cache():
    """Получает данные из кэша, если кэш пуст, получает данные из бд"""
    if not CACHE_ENABLED:
        return Products.objects.all()
    key = 'products_list'
    products = cache.get(key)
    if products is not None:
        return products
    products = Products.objects.all()
    cache.set(key, products)
    return products
