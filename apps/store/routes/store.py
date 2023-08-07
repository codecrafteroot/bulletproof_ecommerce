# builtin imports
from django.urls import path, include

from ..views import store

urlpatterns = [
    path("create", store.create, name="store-create"),
    path("mystore", store.myStore, name="user-store"),
]