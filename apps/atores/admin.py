from django.contrib import admin
from atores.models import Ator
# Register your models here.


@admin.register(Ator)
class AtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nascimento', 'nacionalidade')
