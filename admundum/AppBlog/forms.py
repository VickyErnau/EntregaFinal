from django import forms
from .models import Posteo


class PosteoForm(forms.ModelForm):

    class Meta:
        model = Posteo
        fields = "__all__"

        labels = {
            'titulo': 'Título',
            'resumen' : 'Resúmen',
            'texto' : 'Texto' ,
            'imagen' : 'Imagen',

        }

        widgets  ={
            'titulo' : forms.TextInput(),
            'resumen' : forms.TextInput(),
            'texto' : forms.Textarea(), 
        }
