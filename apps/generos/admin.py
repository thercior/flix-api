from django.contrib import admin
from generos.models import Genero

# Register your models here.
@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

