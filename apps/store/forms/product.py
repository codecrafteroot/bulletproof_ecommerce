# builtin imports
from django import forms

#local imports
from ..models import ProductModel, ProductImageModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'
        exclude = ('uuid', 'owner')


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImageModel
        fields = ['image']