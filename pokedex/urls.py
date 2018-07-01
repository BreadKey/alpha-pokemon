from django.urls import path
from . import views

app_name = 'pokedex'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('pokemon/', views.PokemonIndexView.as_view(), name='pokemon_index'),
    path('pokemon/<int:pk>/', views.PokemonDetailView.as_view(), name='pokemon_detail'),
    path('move/', views.MoveIndexView.as_view(), name='move_index'),
    path('move/<int:pk>/', views.MoveDetailView.as_view(), name='move_detail'),
    path('ability/', views.AbilityIndexView.as_view(), name='ability_index'),
    path('ability/<int:pk>/', views.AbilityDetailView.as_view(), name='ability_detail')
]