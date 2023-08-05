# builtin imports
from django.urls import path, include

urlpatterns = [
    path("products/", include("apps.store.routes.product")),
]