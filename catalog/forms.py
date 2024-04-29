from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        # fields = '__all__'
        exclude = ['owner']

    forbid_words = ("казино", "криптовалюта", "крипта", "биржа", "дешево", "бесплатно", "обман", "полиция", "радар",)

    def clean_name(self):
        cleaned_name = self.cleaned_data['name']
        for name in self.forbid_words:
            if name in cleaned_name:
                raise forms.ValidationError("Недопустимое имя товара")
        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data['description']
        for description in self.forbid_words:
            if description in cleaned_description:
                raise forms.ValidationError(f"Недопустимое описание")
        return cleaned_description


class ProductDeleteForm(forms.Form):
    confirm_delete = forms.BooleanField(label='Подтвердите удаление', required=True)


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
