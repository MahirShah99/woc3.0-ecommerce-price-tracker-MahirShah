from django import forms
from .models import FlipKart

class FlipKartForm(forms.ModelForm):
    class Meta:
        model = FlipKart
        fields = ["url", "desired_price", "email"]