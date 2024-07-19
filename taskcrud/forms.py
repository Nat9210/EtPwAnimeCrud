from django.forms import ModelForm
from .models import *

class CrudForm(ModelForm):
    class Meta:
        model = Media
        fields = ['titulo', 
                'descripcion', 
                'tipo',
                'temporada', 
                'numero_episodios',
                'genero',
                'portada'
                ]
        