# thirdparty imports
from uuid import uuid4

# builtin imports
from django.conf import settings
from django.db import models


class OrderModel(models.Model):
    uuid = models.UUIDField(default=uuid4, unique=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_orders')
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    post_code = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    total_paid = models.DecimalField(max_digits=5, decimal_places=2)
    order_key = models.CharField(max_length=200)
    billing_status = models.BooleanField(default=False)

    class Meta:
        db_table = "orders"
        ordering = ("-created",)
        verbose_name = "Order" 
        verbose_name_plural = "Orders"
	
    def __str__(self):
        return self.name