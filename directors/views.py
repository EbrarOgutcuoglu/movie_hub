# directors/views.py
from django.shortcuts import render, redirect
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