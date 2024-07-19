from django.contrib import admin
from .models import Idioma, Subtitulo, Genero, Episodio, Media

# Register your models here.
admin.site.register(Idioma)
admin.site.register(Subtitulo)
admin.site.register(Genero)
admin.site.register(Episodio)
admin.site.register(Media)