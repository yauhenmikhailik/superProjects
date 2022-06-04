from django import forms
from django.core.exceptions import ValidationError
from apple.models import Product


def valid_name(name):
    if name=="johan":
        print(name)
    else:
        raise ValidationError("error name")

class CategoryForm(forms.Form):
    name = forms.CharField(label='Категория', max_length=100, validators=[valid_name])
    password = forms.CharField(widget=forms.PasswordInput)
    price = forms.DecimalField(max_digits=6,decimal_places=2, label='Цена')

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields=['title','description','price','image','categories','kind','created']