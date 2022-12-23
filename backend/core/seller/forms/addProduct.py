from ..models.Product import Product
from django import forms

class addProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['namaProduct','keterangan']

class addProductImage(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['gambar']