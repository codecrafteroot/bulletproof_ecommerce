# thirdparty imports
from uuid import uuid4

# builtin imports
from django.db import models
from django.utils.translation import gettext_lazy as _


class ProductImageModel(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    product = models.ForeignKey('ProductModel', on_delete=models.SET_NULL, null=True, related_name='product_images')
    image = models.ImageField(_("product image"), upload_to='images/product/picture/', null=True, blank=True)

    class Meta:
        db_table = "product_image"
        ordering = ("uuid",)
        verbose_name = "ProductImage" 
        verbose_name_plural = "ProductImages"