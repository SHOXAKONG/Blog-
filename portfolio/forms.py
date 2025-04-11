from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'last_name', 'email', 'phone_number', 'about']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': True}),
            'phone_number': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Phone Number', 'required': True}),
            'about': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Message', 'required': True}),
        }
