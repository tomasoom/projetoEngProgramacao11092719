from leagueTables import views
from django.urls import path

urlpatterns = [
    path('', views.home_page_view, name="ligas"),
    path('novoClube', views.novoClube_page_view, name="novoClube"),
    path('novaLiga', views.novaLiga_page_view, name="novaLiga"),
    path('liga/<int:liga_id>', views.mostrarLiga_page_view, name="liga"),
    path('jogo/<int:jogo_id>', views.simulaResultado_page_view, name="simulaJogo")
]