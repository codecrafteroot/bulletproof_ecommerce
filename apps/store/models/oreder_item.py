# thirdparty imports
from uuid import uuid4

# builtin imports
from django.db import models


class OrderItemModel(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    order = models.ForeignKey(
        'OrderModel',
        related_name='order_items',
        on_delete=models.CASCADE
    )
    product = models.ForeignKey(
        'ProductModel',
        related_name='product_items',
        on_delete=models.CASCADE
    )
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "order_item"
        ordering = ("uuid",)
        verbose_name = "OrderItem" 
        verbose_name_plural = "OrderItems"

    def __str__(self):
        return str(self.uuid)