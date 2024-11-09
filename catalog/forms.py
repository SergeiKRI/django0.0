from django.forms import ModelForm, forms, BooleanField

from catalog.models import Products, Version


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs["class"] = "form-check-input"
            else:
                fild.widget.attrs["class"] = "form-control"


class ProductsForm(ModelForm, StyleMixin):
    BANNED = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    class Meta:
        model = Products
        exclude = (
            "date_created_at",
            "date_updated_at",
        )

    def _clean_name(self):
        name = self.cleaned_data["name"]
        if name.lower() in self.BANNED:
            raise forms.ValidationError("Использованны запрещенные слова")
        return name

    def _clean_description(self):
        description = self.cleaned_data["description"]
        if description.lower() in self.BANNED:
            raise forms.ValidationError("Использованны запрещенные слова")
        return description


class VersionForm(ModelForm, StyleMixin):
    class Meta:
        model = Version
        fields = "__all__"
