from django import forms

class MangaFormulario(forms.Form):
    manga = forms.CharField()
    genero = forms.CharField()
    anio_lanzamiento = forms.IntegerField()
    tomo = forms.IntegerField()
