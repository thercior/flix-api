from django.db import models

# Create your models here.

NACIONALIDADE_CHOICES = (
    ('EUA', 'Estados Unidos'),
    ('BRA', 'Brasil'),
    ('ING', 'Inglaterra'),
    ('ARG', 'Argentina'),
    ('GER', 'Alemanha'),
    ('AUS', 'Austrália'),
    ('HOL', 'Holanda'),
    ('ESP', 'Espanha'),
)

class Ator(models.Model):
    nome = models.CharField(max_length=200)
    nascimento = models.DateField(null=True, blank=True)
    nacionalidade = models.CharField(max_length=100, choices=NACIONALIDADE_CHOICES, blank=True, null=True)
    
    def __str__(self):
        return self.nome
