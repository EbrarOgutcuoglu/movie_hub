# directors/forms.py
from django import forms
from .models import Director

class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ['name', 'bio', 'birth_date', 'image_url']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#40bcf4]'}),
            'bio': forms.Textarea(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#40bcf4]', 'rows': 4}),
            'birth_date': forms.DateInput(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#40bcf4]', 'type': 'date'}),
            'image_url': forms.URLInput(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#40bcf4]'}),
        }