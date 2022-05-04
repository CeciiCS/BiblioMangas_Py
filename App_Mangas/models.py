from cgitb import text
from tabnanny import verbose
from django.db import models

# Create your models here.

class Manga(models.Model):
    nombre = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    anio_lanzamiento = models.IntegerField()
    tomo = models.IntegerField()

    def __str__(self) -> str:
        txt="{0} - {1}"
        return txt.format(self.nombre, self.genero)

class Autor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self) -> str:
        txt="{0} - {1}"
        return txt.format(self.nombre, self.apellido)

class Personaje(models.Model):
    nombre_completo = models.CharField(max_length=60)
    fecha_nacimiento = models.DateField()
    nombre_manga = models.CharField(max_length=20)

    def __str__(self) -> str:
        txt="{0} - {1}"
        return txt.format(self.nombre_completo, self.nombre_manga)

