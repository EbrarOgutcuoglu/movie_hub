from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .form import MovieForm
from directors.models import Director

def movie_list(request):
    movies = Movie.objects.all().order_by('-id') # Newest first
    directors = Director.objects.all().order_by('name')
    selected_director = request.GET.get('director')


    if selected_director:
        movies = movies.filter(director_id=selected_director)

    return render(request, 'movies/movie_list.html', {
        'movies': movies,
        'directors': directors,
        'selected_director': selected_director  # it is render selected director
    })

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

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})