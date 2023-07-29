
from django.urls import path
from Control import views




urlpatterns = [
    path('Inicio', views.Inicio,name="Inicio"),
    path('Tenis',views.InscribirseTenis, name="Tenis"),
    path('Basquet',views.InscribirseBasquet, name="Basquet"),
    path('Rugby',views.InscribirseRugby, name="Rugby"),
    path('Futbol',views.InscribirseFutbol, name="Futbol"),
    path('Jugadores',views.listar_jugadores, name="Jugadores"),
    path('Buscarjugadores',views.buscar_jugadores, name="Buscarjugadores")

]

