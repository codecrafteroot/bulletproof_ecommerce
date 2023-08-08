# builtin imports
from django import forms
from django.utils.translation import gettext_lazy as _

class SignupCompletedForm(forms.Form):
    customer = forms.BooleanField(label=_("Customer or Saleor"), required=True)