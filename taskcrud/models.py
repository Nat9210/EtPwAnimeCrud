from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.db import models

class Idioma(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Subtitulo(models.Model):
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
    
class Episodio(models.Model):
    nombre = models.CharField(max_length=100)
    numero = models.IntegerField()
    descripcion = models.TextField(null=True, blank=True)
    archivo = models.FileField(upload_to='episodios/', null=True, blank=True)
    duracion = models.DurationField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre

class Media(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    TIPO_CHOICES = (
        ('serie', 'Serie'),
        ('pelicula', 'Película')
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    fecha_transmision = models.IntegerField(null=True, blank=True)
    temporada = models.IntegerField(null=True, blank=True)
    numero_episodios = models.IntegerField(null=True, blank=True)
    episodios = models.ManyToManyField(Episodio, blank=True)
    duracion_capitulo = models.DurationField(null=True, blank=True)
    calidad = models.CharField(max_length=20, null=True, blank=True)
    idiomas = models.ManyToManyField(Idioma)
    subtitulo = models.ManyToManyField(Subtitulo)
    genero = models.ManyToManyField(Genero)
    portada = models.ImageField(upload_to='portadas/', null=True, blank=True)
    

    def __str__(self):
        return self.titulo