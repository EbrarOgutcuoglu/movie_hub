# directors/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Director
from .forms import DirectorForm

def director_list(request):
    directors = Director.objects.all().order_by('name')
    return render(request, 'directors/director_list.html', {'directors': directors})

def director_create(request):
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('director_list')
    else:
        form = DirectorForm()
    return render(request, 'directors/director_form.html', {'form': form})

def director_detail(request, pk):
    director = get_object_or_404(Director, pk=pk)
    # Fetching all movies related to this director via foreign key reverse lookup
    movies = director.movies.all()
    return render(request, 'directors/director_detail.html', {'director': director, 'movies': movies})

def director_delete(request, pk):
    director = get_object_or_404(Director, pk=pk)
    if request.method == 'POST':
        director.delete()  # CASCADE sayesinde filmleri de silinecek!
        return redirect('director_list')
    return render(request, 'directors/director_confirm_delete.html', {'director': director})