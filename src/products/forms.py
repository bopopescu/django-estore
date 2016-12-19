from django import forms
from django.forms.models import modelformset_factory

from .models import Variation

class VaraitionInventoryForm(forms.ModelForm):
    class Meta:
        model = Variation
        fields = [
            "title",
            "price",
            "sale_price",
            "inventory",
            "active"
        ]

VaraitionInventoryFormSet = modelformset_factory(Variation, form=VaraitionInventoryForm, extra=0)
