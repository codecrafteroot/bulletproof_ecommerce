# thirdparty imports
from uuid import uuid4

# builtin imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe

class CategoryModel(models.Model):
	uuid = models.UUIDField(default=uuid4, unique=True)
	name = models.CharField(max_length=200)
	description = models.TextField()  
    
	class Meta:
		db_table = "category"
		ordering = ("uuid",)
		verbose_name = "Category" 
		verbose_name_plural = "Categories"
	
	def __str__(self):
		return self.name