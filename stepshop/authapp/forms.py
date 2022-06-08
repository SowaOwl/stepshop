from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from authapp.models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=128,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'Login',
            }
        )
    )

    class Meta:
        model = ShopUser
        fields = {'username', 'password'}

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)

        for field_name, field_value in self.fields.items():
            field_value.widget.attrs['class'] = 'form-control'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = {'username', 'first_name', 'password1', 'password2', 'email', 'age', 'avatar'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field_value in self.fields.items():
            field_value.widget.attrs['class'] = 'form-control'

    def clean_age(self):
        data = self.cleaned_data['age']

        if data < 18:
            raise forms.ValidationError('Age Error')

        return data
