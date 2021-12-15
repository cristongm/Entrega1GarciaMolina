from django.shortcuts import render
from django.http import HttpResponse
# from .models import Estadio, Equipo, Jugador
# from .forms import EstadioFormulario, JugadorFormulario

def inicio(request):
    return render(request, 'App/inicio.html')
#----RUTAS PARA EVENTOS----
def eventos(request):
    return render(request, 'App/eventos.html')
#----FIN RUTAS PARA EVENTOS----

#----RUTAS PARA Bandas----
def bandas(request):
    # return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'App/bandas.html')
#----FIN RUTAS PARA Bandas----

#----RUTAS PARA Instrumentos----
def instrumentos(request):
    # return HttpResponse("Esto es una prueba del inicio")
    return render(request, 'App/instrumentos.html')
#----FIN RUTAS PARA Instrumentos----