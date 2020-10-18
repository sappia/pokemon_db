from django.contrib import admin
from django.urls import path
from pokedex import views
import pokedex.api_views

# url patterns to access all pokemon details, expose apis and admin page
urlpatterns = [
    path('api/v1/pokemons/', pokedex.api_views.PokemonList.as_view()),
    path('api/v1/pokemons/new/', pokedex.api_views.PokemonCreate.as_view()),
    path('api/v1/pokemons/<int:number>/', pokedex.api_views.PokemonRetrieveUpdateDestroy.as_view()),
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('pokedex/<int:pokemon_id>/', views.pokemon_detail, name='pokemon_detail'),
]
