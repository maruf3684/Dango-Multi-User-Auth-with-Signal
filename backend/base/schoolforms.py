from .models import Account
from django.forms import ModelForm


class UserForm(ModelForm):
    class Meta:
         model = Account
         fields = ['name','email','password']
