from django import forms
from .models import Amazon

class AmazonForm(forms.ModelForm):
    class Meta:
        model = Amazon
        # fields = ["desired_price", "email"]
        exclude = ['date_time']