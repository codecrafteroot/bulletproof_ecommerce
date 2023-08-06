# builtin imports
from django.urls import path, include

from ..views import product

urlpatterns = [
    # ex: /products/
    # path("list", product.index, name="index"),
    path("create", product.create, name="product-create"),
    path("add_image/<int:product_id>/", product.add_images, name="product-add-images"),
    # ex: /products/5/
    path("detail/<int:product_id>/", product.detail, name="product-detail"),
]