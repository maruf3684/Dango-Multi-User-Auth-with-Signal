from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import Account


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=Account
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model=Account
        fields = '__all__'