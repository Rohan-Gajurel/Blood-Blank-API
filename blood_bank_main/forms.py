from .models import BloodRequest
from django import forms

class BloodRequestForm(forms.ModelForm):
    class Meta:
        model= BloodRequest
        fields = [ 'phone_number', 'blood_group_required', 'quantity_required']
        widgets = {
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'blood_group_required': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity_required': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity required'}),
        }
