# thirdparty imports
from uuid import uuid4

# builtin imports
from django.db import models
from django.utils.translation import gettext_lazy as _

class StoreModel(models.Model):
	uuid = models.UUIDField(default=uuid4, unique=True)
	name = models.CharField(max_length=200)
	description = models.TextField()

	owner = models.ForeignKey('accounts.UserModel', on_delete=models.CASCADE, related_name='user_stores')  
    
	class Meta:
		db_table = "store"
		ordering = ("uuid",)
		verbose_name = "Store" 
		verbose_name_plural = "Stores"
	
	def __str__(self):
		return self.name