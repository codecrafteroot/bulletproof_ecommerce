# builtin imports
from django.urls import path, include

from ..views import product

urlpatterns = [
    # ex: /products/
    # path("list", product.index, name="index"),
    # ex: /products/5/
    path("detail/<int:product_id>/", product.detail, name="product-detail"),
]