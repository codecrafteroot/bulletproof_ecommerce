# builtin imports
from django.urls import path, include

from ..views import product

urlpatterns = [
    path("list",                              product.list,           name="product-list"),
    path("listbycategory/<int:category_id>/", product.listByCategory, name="category-products"),
    path("create",                            product.create,         name="product-create"),
    path("add_image/<int:product_id>/",       product.add_images,     name="product-add-images"),
    path("detail/<int:product_id>/",          product.detail,         name="product-detail"),
]