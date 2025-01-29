from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Posteo(models.Model):
    titulo = models.CharField(max_length=250)
    resumen = models.CharField(max_length=150,null=True, blank=True)
    texto = RichTextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    imagen = models.ImageField(upload_to="posts", null=True, blank=True)
    #autor = models.ForeignKey(Autor, on_delete=models.CASCADE, default=None)

    def _str_(self):
        return f'{self.titulo}'


