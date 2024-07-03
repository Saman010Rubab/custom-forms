from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    def clean_name(self):
        name= self.cleaned_data.get('name')
        if not self.instance.pk :
            if Product.objects.filter(name=name).exists():
                raise forms.ValidationError("Product with this name already exists.")
            return name
        else:
            return name

    def clean_quantity(self):
        quantity= self.cleaned_data.get('quantity')
        if quantity < 0:
            raise forms.ValidationError("Quantity can't be less than zero.")
        return quantity

    def clean_image(self):
        image= self.cleaned_data.get('image')
        if not self.instance.pk :
            if image.size > 2 * 1024 * 1024:
                raise forms.ValidationError("Image file size must be greater than 2MB.")
            return image
        else:
            return image