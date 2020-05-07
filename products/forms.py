from django import forms

from .models import Product, Producttype


class ProductForm(forms.ModelForm):
    producttype = forms.ModelChoiceField(queryset=Producttype.objects, required=True)
    title = forms.CharField(label='Enter Title', widget=forms.TextInput(attrs={
        "placeholder": "Your Title"
    }))
    description = forms.CharField(
        required=False,
        label='Enter Description',
        widget=forms.Textarea(
            attrs={
                "placeholder": "Your Description",
                "class": "new-class-name",
                "id": "description",
                "rows": 8,
                "cols": 60,
            }
        )
    )
    price = forms.DecimalField(label='Enter Price', initial=50)
    summary = forms.CharField(label='Enter Summary', required=False)
    featured = forms.BooleanField(label='Is It Featured', required=False)

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'summary',
            'featured',
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "bad" in title:
            return title
        else:
            raise forms.ValidationError("this is not a valid title")

    def clean_price(self, *args, **kwargs):
        price = self.cleaned_data.get("price")
        if price < 50:
            raise forms.ValidationError("Price is too less")
        else:
            return price


class RawProductForm(forms.Form):
    title = forms.CharField(label='Enter Title', widget=forms.TextInput(attrs={
        "placeholder": "Your Title"
    }))
    description = forms.CharField(
                        required=False,
                        label='Enter Description',
                        widget=forms.Textarea(
                            attrs={
                                "placeholder": "Your Description",
                                "class": "new-class-name",
                                "id": "description",
                                "rows": 8,
                                "cols": 60,
                            }
                        )
                    )
    price = forms.DecimalField(label='Enter Price', initial=50)
    summary = forms.CharField(label='Enter Summary', required=False)
    featured = forms.BooleanField(label='Is It Featured', required=False)
