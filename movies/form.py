# movies/forms.py
from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    # Defining specific choice scores to display as stylized bubbles or stars
    RATING_CHOICES = [
        (0.5, '½ '),
        (1.0, '★ '),
        (1.5, '★½ '),
        (2.0, '★★ '),
        (2.5, '★★½ '),
        (3.0, '★★★ '),
        (3.5, '★★★½ '),
        (4.0, '★★★★ '),
        (4.5, '★★★★½ '),
        (5.0, '★★★★★ '),
    ]

    rating = forms.ChoiceField(
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'hidden-radio'}), # Custom layout via css/tailwind
        initial=3.0,
        help_text="Select a bubble score or type it manually below."
    )

    GENRE_CHOICES = [
        ('', 'Select a Genre'),
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Animation', 'Animation'),
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Horror', 'Horror'),
        ('Romance', 'Romance'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Thriller', 'Thriller'),
        ('Western', 'Western'),

        ('Documentary', 'Documentary'),
    ]
    genre = forms.ChoiceField(
        choices=GENRE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#00e054]'})
    )

    class Meta:
        model = Movie
        fields = ['title', 'director','actor', 'comment', 'genre', 'rating', 'poster_url', 'release_date', 'trailer_url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#00e054]'}),
            'director': forms.Select(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#00e054]'}),
            'actor': forms.CheckboxSelectMultiple(attrs={'class': 'text-white bg-[#14181c]'}),
            'comment': forms.Textarea(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#00e054]', 'rows': 4}),
            'poster_url': forms.URLInput(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#00e054]'}),
            'trailer_url': forms.URLInput(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#00e054]','placeholder': 'https://www.youtube.com/embed/...'  }),
            'release_date': forms.DateInput(attrs={'class': 'w-full bg-[#2c3440] border border-gray-700 rounded p-2.5 text-white focus:outline-none focus:border-[#00e054]', 'type': 'date'}),
        }