from django.contrib import admin

# Register your models here.
from .models import *

class ProductAdmin(admin.ModelAdmin):
    list_display = ["picture_preview", "name"]
    readonly_fields = ['picture_preview']

admin.site.register(ProductModel, ProductAdmin)
admin.site.register(ProductImageModel)
admin.site.register(CategoryModel)
admin.site.register(StoreModel)
admin.site.register(OrderModel)
admin.site.register(OrderItemModel)