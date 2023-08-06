# builtin imports
from django import forms

#local imports
from ..models import UserModel

class UserChangeForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'
        exclude = ('uuid', 'password', 'last_login', 'date_joined', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')