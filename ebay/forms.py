from django import forms
from .models import Ebay

class EbayForm(forms.ModelForm):
    class Meta:
        model = Ebay
        fields = ["url", "desired_price", "email"]