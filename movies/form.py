# movies/forms.py
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    # Defining specific choice scores to display as stylized bubbles or stars
    RATING_CHOICES = [
        (1.0, '★ (1.0)'),
        (2.0, '★★ (2.0)'),
        (3.0, '★★★ (3.0)'),
        (4.0, '★★★★ (4.0)'),
        (5.0, '★★★★★ (5.0)'),
    ]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'hidden-radio'}), # Custom layout via css/tailwind
        initial=3.0,
        help_text="Select a bubble score or type it manually below."
    )

    class Meta:
        model = Movie
        fields = ['title', 'director', 'description', 'genre', 'rating', 'poster_url', 'release_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#00e054]'}),
            'director': forms.Select(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#00e054]'}),
            'description': forms.Textarea(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#00e054]', 'rows': 4}),
            'genre': forms.TextInput(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#00e054]', 'placeholder': 'e.g. Sci-Fi, Drama'}),
            'poster_url': forms.URLInput(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#00e054]'}),
            'release_date': forms.DateInput(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#00e054]', 'type': 'date'}),
        }