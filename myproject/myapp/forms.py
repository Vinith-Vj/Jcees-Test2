from django import forms
from .models import Contacts

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['first_name', 'last_name', 'email', 'package_type', 'phone', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline-1 outline-gray-300'}),
            'last_name': forms.TextInput(attrs={'class': 'block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline-1 outline-gray-300'}),
            'email': forms.EmailInput(attrs={'class': 'block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline-1 outline-gray-300'}),
            'package_type': forms.Select(attrs={'class': 'block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline-1 outline-gray-300'}),
            'phone': forms.TextInput(attrs={'class': 'block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline-1 outline-gray-300'}),
            'message': forms.Textarea(attrs={'class': 'block w-full rounded-md bg-white px-3.5 py-2 text-base text-gray-900 outline-1 outline-gray-300 h-[150px] sm:h-[250px]'}),
        }
