from django.urls import path
from . import views

urlpatterns = [
    path('', views.actor_list, name='actor_list'),
    path('create/', views.actor_create, name='actor_create'),
    path('<int:pk>/', views.actor_detail, name='actor_detail'),
    path('<int:pk>/edit/', views.actor_update, name='actor_update'),
    path('<int:pk>/delete/', views.actor_delete, name='actor_delete'),
]