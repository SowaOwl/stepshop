from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

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
    password1 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'id': 'password1'
            }
        )
    )

    password2 = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                'id': 'password2'
            }
        )
    )

    age = forms.IntegerField(
        validators=[MaxValueValidator(100),
                    MinValueValidator(0)],
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Age',
                'id': 'age',
                'min': 0,
                'max': 100,
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
                'id': 'email',
            }
        )
    )

    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Username',
                'id': 'username',
            }
        )
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Name',
                'id': 'username',
            }
        )
    )

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


class ShopUserEditForm(UserChangeForm):
    class Meta:
        model = ShopUser
        fields = {'username', 'first_name', 'email', 'age', 'avatar', 'password'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_value in self.fields.items():
            field_value.widget.attrs['class'] = 'form-control'
            field_value.help_text = ''

            if field_name == 'password':
                field_value.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']

        if data < 18:
            raise forms.ValidationError('Age Error')

        return data
