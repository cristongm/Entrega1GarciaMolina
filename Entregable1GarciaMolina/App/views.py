from django.shortcuts import render
from django.http import HttpResponse
from .models import Evento, Banda, Instrumento
from .forms import EventosFormulario, BandasFormulario, InstrumentosFormulario

def inicio(request):
    return render(request, 'App/inicio.html')
#----RUTAS PARA EVENTOS----
def eventos(request):
    if(request.method == 'POST'):
        miFormulario = EventosFormulario(request.POST)
        
        if(miFormulario.is_valid()):
            informacion = miFormulario.cleaned_data
            evento = Evento(
                nombre = informacion["nombre"],
                ciudad = informacion["ciudad"],
                fecha = informacion["fecha"],
                valorEntrada = informacion["valorEntrada"]
            )
            evento.save()
            # Reseteo de formulario si todo sale bien
            miFormulario = EventosFormulario()
        return render(request, 'App/eventos.html', {"miFormulario":miFormulario})
        
    elif('nombre' in request.GET ):
        miFormulario = EventosFormulario()
        nombre = request.GET['nombre']
        eventos = Evento.objects.filter(nombre__icontains = nombre)
        return render(request, 'App/eventos.html', {"eventos":eventos, "miFormulario":miFormulario})
    else:
        miFormulario = EventosFormulario()
        return render(request, 'App/eventos.html', {"miFormulario":miFormulario})
#----FIN RUTAS PARA EVENTOS----

#----RUTAS PARA Bandas----
def bandas(request):
    if(request.method == 'POST'):
        miFormulario = BandasFormulario(request.POST)
        
        if(miFormulario.is_valid()):
            informacion = miFormulario.cleaned_data
            banda = Banda(
                nombre = informacion["nombre"],
                tipoMusica = informacion["tipoMusica"],
                ciudad = informacion["ciudad"],
                descripcion = informacion["descripcion"]
            )
            banda.save()
            # Reseteo de formulario si todo sale bien
            miFormulario = BandasFormulario()
        return render(request, 'App/bandas.html', {"miFormulario": miFormulario})
    elif('nombre' in request.GET ):
        miFormulario = BandasFormulario()
        nombre = request.GET['nombre']
        bandas = Banda.objects.filter(nombre__icontains = nombre)
        return render(request, 'App/bandas.html', {"bandas":bandas, "miFormulario":miFormulario})
    else:
        miFormulario = BandasFormulario()
        return render(request, 'App/bandas.html',{"miFormulario":miFormulario})
#----FIN RUTAS PARA Bandas----

#----RUTAS PARA Instrumentos----
def instrumentos(request):
    if(request.method == 'POST'):
        miFormulario = InstrumentosFormulario(request.POST)
        
        if(miFormulario.is_valid()):
            informacion = miFormulario.cleaned_data
            instrumento = Instrumento(
                nombre = informacion['nombre'],
                tipoInstrumento = informacion['tipoInstrumento'],
                propietario = informacion['propietario'],
                enVenta = informacion['enVenta']
            )
            instrumento.save()
            # Reseteo de formulario si todo sale bien
            miFormulario = InstrumentosFormulario()
        return render(request, 'App/instrumentos.html', {"miFormulario":miFormulario})
    elif('nombre' in request.GET ):
        miFormulario = InstrumentosFormulario()
        nombre = request.GET['nombre']
        instrumentos = Instrumento.objects.filter(nombre__icontains = nombre)
        return render(request, 'App/instrumentos.html', {"instrumentos":instrumentos, "miFormulario":miFormulario})
    else:
        miFormulario = InstrumentosFormulario()
        return render(request, 'App/instrumentos.html', { "miFormulario":miFormulario})
#----FIN RUTAS PARA Instrumentos----