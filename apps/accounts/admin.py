from django.contrib import admin

# Register your models here.
from .models import UserModel

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["picture_preview", "username", "email", "is_active"]
    readonly_fields = ['picture_preview']
    list_filter = ["is_active", "date_joined"]
    search_fields = ["last_name", "first_name"]

admin.site.register(UserModel, CustomUserAdmin)