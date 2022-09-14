from statistics import mode
from tabnanny import verbose
from turtle import title
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    public = models.BooleanField(default=0, verbose_name="Artículo publicado")
    cratead_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated_at = models.DateTimeField(auto_now=True,verbose_name="Editado")

    class Meta():
        verbose_name= 'Articulo'
        verbose_name_plural = 'Articulos'
    
    def __str__(self):

        if self.public:
            public = "Publicado"
        else:
            public = "Privado"

        return f"{self.title} ({public})" 



class Categoria(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    cratead_at = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta():
        verbose_name= 'Categoria'
        verbose_name_plural = 'Categorias'