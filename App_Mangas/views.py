from django.shortcuts import render
from App_Mangas.models import Manga
from App_Mangas.forms import MangaFormulario

# Create your views here.

def inicio(request):

    return render(request, "App_Mangas/inicio.html")

def manga(request):

    return render(request, "App_Mangas/manga.html")

def autor(request):

    return render(request, "App_Mangas/autor.html")

def personaje(request):

    return render(request, "App_Mangas/personaje.html")

def mangaFormulario(request):
    if request.method == "POST":
        mangaForm = MangaFormulario(request.POST)
        print(mangaForm)
        if mangaForm.is_valid:
            informacion = mangaForm.cleaned_data
            manga = Manga (nombre=informacion['nombre'], genero=informacion['genero'], anio_lanzamiento=informacion['anio_lanzamiento'], tomo=informacion['tomo'])
            manga.save()
            return render(request, "App_Mangas/inicio.html")
    else:
        mangaForm = MangaFormulario()
    return render(request, "App_Mangas/mangaFormulario.html", {"mangaForm": mangaForm})
