from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .form import MovieForm

def movie_list(request):
    movies = Movie.objects.all().order_by('-id') # Newest first
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieForm()
    return render(request, 'movies/movie_form.html', {'form': form})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})