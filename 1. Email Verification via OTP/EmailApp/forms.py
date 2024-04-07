from .models import Subscribers
from django import forms

class Subscribe(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = "__all__"

class OTPform(forms.Form):
    OTP = forms.IntegerField()
