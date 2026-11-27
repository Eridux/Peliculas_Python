from django.shortcuts import render
from .services import ver_peliculas

type Valor = str | list | None
# Create your views here.
def inicio(request):
    #tarjetas: list[int]= list (range(1,21))
    
    params: dict[str, int] = {
        'genres': 28,
        'page': 1
    }
    datos: dict[str, Valor]= {
        'titulo': 'Página de Inicio',
        'encabezado': 'Bienvenidos al portal de películas',
       # 'tarjetas': tarjetas,
        'peliculas': ver_peliculas(params),
        'images': 'https://image.tmdb.org/t/p/w400'
    }
    
    return render(request, 'peliculas/index.html', datos)