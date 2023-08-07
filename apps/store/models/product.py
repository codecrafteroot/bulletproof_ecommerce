# thirdparty imports
from uuid import uuid4

# builtin imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.html import mark_safe

class ProductModel(models.Model):
	uuid = models.UUIDField(default=uuid4, unique=True)
	name = models.CharField(max_length=200)
	price = models.FloatField()
	digital = models.BooleanField(default=False,null=True, blank=True)
	principale_image = models.ImageField(_("product image"), upload_to='images/product/picture/', default='defaults/product_default.png')  

	category = models.ForeignKey('CategoryModel', on_delete=models.SET_NULL, null=True, related_name='products')  
    
	class Meta:
		db_table = "products"
		ordering = ("uuid",)
		verbose_name = "Product" 
		verbose_name_plural = "Products"
	
	def __str__(self):
		return self.name
	
	def picture_preview(self): #new
		return mark_safe('<img src = "{url}" width = "50"/>'.format(
             url = self.principale_image.url
        ))
    