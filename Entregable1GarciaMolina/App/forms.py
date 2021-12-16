from django import forms

class EventosFormulario(forms.Form):
    nombre = forms.CharField(max_length=45)
    ciudad = forms.CharField(max_length=45)
    fecha = forms.DateTimeField(label=("Fecha (AAAA-MM-DD)"))
    valorEntrada = forms.IntegerField(label="Valor Entrada")
    
class BandasFormulario(forms.Form):
    nombre = forms.CharField(max_length=45)
    tipoMusica = forms.CharField(label="Tipo de Música",max_length=45)
    ciudad = forms.CharField(max_length=45)
    descripcion = forms.CharField(max_length=45)

class InstrumentosFormulario(forms.Form):
    nombre = forms.CharField(max_length=45)
    tipoInstrumento = forms.CharField(label="Tipo Instrumento: ", max_length=45)
    propietario = forms.CharField(max_length=45)
    enVenta = forms.BooleanField(label="En venta: ", required=False)
    