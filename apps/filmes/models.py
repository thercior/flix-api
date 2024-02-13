from django.db import models
from generos.models import Genero
from atores.models import Ator


class Filme(models.Model):
    titulo = models.CharField(max_length=500)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT, related_name='filme')
    ano = models.DateField(null=True, blank=True)
    atores = models.ManyToManyField(Ator, related_name='filme')
    resumo = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo
