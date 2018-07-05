from django.urls import path
from . import views

app_name = 'sample_maker'

urlpatterns = [
    path('', views.SelectPokemonView.as_view(), name='select_pokemon'),
    path('<int:pk>/', views.SampleMakerView.as_view(), name='sample_maker')
]