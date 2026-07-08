# directors/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.director_list, name='director_list'),
    path('add/', views.director_create, name='director_create'),
    path('<int:pk>/', views.director_detail, name='director_detail'),
]