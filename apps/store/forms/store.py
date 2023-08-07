# builtin imports
from django import forms

#local imports
from ..models import StoreModel

class StoreForm(forms.ModelForm):
    class Meta:
        model = StoreModel
        fields = '__all__'
        exclude = ('uuid', 'owner')