from rest_framework import generics
from .models import Pokemon
from .serializers import PokemonSerializer

class PokemonListCreate(generics.ListCreateAPIView):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
