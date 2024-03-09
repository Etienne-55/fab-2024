from django.urls import path
from .views import PokemonListCreate

urlpatterns = [
    path('', PokemonListCreate.as_view(), name='pokemon-list-create'),
]
