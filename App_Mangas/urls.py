from django.urls import path
from App_Mangas import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('mangas/', views.manga, name="Mangas"),
    path('autores/', views.autor, name="Autores"),
    path('personajes/', views.personaje, name="Personajes"),
    path('mangaFormulario/', views.mangaFormulario, name="MangaFormulario"),
]