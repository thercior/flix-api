from django.contrib import admin
from filmes.models import Filme

# Register your models here.
@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'genero', 'ano', 'resumo')