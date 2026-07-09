from django.shortcuts import render, redirect, get_object_or_404
from .models import Actor
from .forms import ActorForm

# 1. List Page
def actor_list(request):
    actors = Actor.objects.all()
    return render(request, 'actor/actor_list.html', {'actors': actors})

# 2. Detail Page
def actor_detail(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    return render(request, 'actor/actor_detail.html', {'actor': actor})

# 3. Create (Add) Page
def actor_create(request):
    if request.method == 'POST':
        form = ActorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('actor_list')
    else:
        form = ActorForm()
    return render(request, 'actor/actor_form.html', {'form': form, 'title': 'Add New Actor'})

# 4. Update (Edit) Page
def actor_update(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    if request.method == 'POST':
        form = ActorForm(request.POST, instance=actor)
        if form.is_valid():
            form.save()
            return redirect('actor_detail', pk=actor.pk)
    else:
        form = ActorForm(instance=actor)
    return render(request, 'actor/actor_form.html', {'form': form, 'title': 'Edit Actor'})

# 5. Delete Page
def actor_delete(request, pk):
    actor = get_object_or_404(Actor, pk=pk)
    if request.method == 'POST':
        actor.delete()
        return redirect('actor_list')
    return render(request, 'actor/actor_confirm_delete.html', {'actor': actor})