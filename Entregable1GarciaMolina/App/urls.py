from django.urls import path
from App import views

urlpatterns= [
    # path('admin/', admin.site.urls),
    path('', views.inicio, name="Inicio"),
    path('eventos', views.eventos, name="Eventos"),
    path('eventos/', views.eventos, name="EventosBuscar"),
    path('bandas', views.bandas, name="Bandas"),
    path('bandas/', views.bandas, name="BandasBuscar"),
    path('instrumentos', views.instrumentos, name="Instrumentos"),
    path('instrumentos/', views.instrumentos, name="InstrumentosBuscar")
]