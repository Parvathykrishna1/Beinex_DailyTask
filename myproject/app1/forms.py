from django import forms
from .models import Category, Product

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

class RegularProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    created_at = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    updated_at = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    image = forms.FileField()

class ModelProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image']

