from django import forms
from .models import Actor


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'age',  'photo_url']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'bg-[#14181c] border border-gray-700 text-white rounded p-2.5 w-full focus:outline-none focus:border-[#00e054]'
            }),
            'age': forms.NumberInput(attrs={
                'class': 'bg-[#14181c] border border-gray-700 text-white rounded p-2.5 w-full focus:outline-none focus:border-[#00e054]',
                'min': '0',
                'max': '120',
                'placeholder': 'ex: 28'
            }),
            'photo_url': forms.URLInput(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#40bcf4]'}),
        }