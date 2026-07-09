from django.shortcuts import render, redirect, get_object_or_404
from .models import Movie
from .form import MovieForm
from directors.models import Director

def movie_list(request):
    movies = Movie.objects.all().order_by('-id') # Newest first
    directors = Director.objects.all().order_by('name')
    selected_director = request.GET.get('director')
    print("abc")
    print(selected_director)

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
            movie = form.save(commit=False)
            movie.save()

            form.save_m2m()
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


def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        # DİKKAT 1: request.FILES eklendi (Afişlerin bozulmaması için)
        form = MovieForm(request.POST, request.FILES, instance=movie)

        # DİKKAT 2: Tarayıcının gönderdiği veriyi terminale yazdırıyoruz
        print("TARAYICIDAN GELEN VERİLER:", request.POST)

        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            form.save_m2m()
            return redirect('movie_detail', pk=movie.pk)
        else:
            print("FORM HATALARI:", form.errors)  # Eğer form arka planda patlıyorsa görelim
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form, 'title': 'Edit Movie'})