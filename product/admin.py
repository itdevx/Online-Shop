from django.contrib import admin
from product.models import Product, Category


@admin.register(Product)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'status']
    list_filter = ['title', 'date', 'status']
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(Category)