from django.contrib import admin
from .models import Product, Category


class ItemInline(admin.StackedInline):
    model = Product
    extra = 1
    autocomplete_fields = ('category',)


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    inlines = [ItemInline]
    search_fields = ('title',)


@admin.register(Product)
class EstateAdmin(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ('id',)
    search_fields = ('title',)
