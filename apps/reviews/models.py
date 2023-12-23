from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from filmes.models import Filme

# Create your models here.
class Review(models.Model):
    filme = models.ForeignKey(Filme, on_delete=models.PROTECT, related_name='reviews')
    stars = models.IntegerField(
        validators=[
            MinValueValidator(0, 'Avalição não pode ser inferior a 0 estrelas'),
            MaxValueValidator(5, 'Avalição não pode ser superior a 5 estrelas'),
        ]
    )
    comentario = models.TextField(blank=True, null=True)