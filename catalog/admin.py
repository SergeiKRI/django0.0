from django.contrib import admin

from catalog.models import Category, Products, BlogRecord, Version


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', 'date_updated_at',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(BlogRecord)
class BlogRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'date_created_at', 'count_views')
    list_filter = ('is_active',)
    search_fields = ('title', 'slug', 'text',)


@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_ver')
