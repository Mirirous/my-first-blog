from django.contrib import admin
from StoreWeb.models import Product
from StoreWeb.models import Price
from StoreWeb.models import Post

admin.site.register(Post)


class PriceAdminInline(admin.TabularInline):
    model = Price


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'quantity')
    search_fields = ('name', 'description')
    list_filter = ('name', 'description')
    inlines = (PriceAdminInline,)


admin.site.register(Product, ProductAdmin)
