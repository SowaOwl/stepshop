from django.contrib.auth.forms import AuthenticationForm

from authapp.models import ShopUser


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = {'username', 'password'}

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field_value in self.fields.items():
            field_value.widget.attrs['class'] = 'form-control'
