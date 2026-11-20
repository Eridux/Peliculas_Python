from django.shortcuts import render

# Create your views here.
def inicio(request):
    datos: dict[str, str]= {
        'titulo': 'Página de Inicio',
        'encabezado': 'Bienvenidos al portal de películas',
    }
    
    return render(request, 'peliculas/index.html', datos)