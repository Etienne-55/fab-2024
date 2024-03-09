from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import PokemonSerializer
import requests

class PokemonCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        
        response = requests.get('https://pokeapi.co/api/v2/pokemon/1/')
        
        if response.status_code == 200:
            data = response.json()
            
          
            pokemon_data = {
                'name': data['name'],
                'tyipe': data['type'],
                'abillities': data['abillities'],
                'stats': data['stats']
               
            }
            
            serializer = PokemonSerializer(data=pokemon_data)
            
            if serializer.is_valid():
               
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Falha ao obter dados da API de Pokémon'}, status=response.status_code)
