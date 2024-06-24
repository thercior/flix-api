from django.contrib import admin
from reviews.models import Review


@admin.register(Review)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'filme', 'stars', 'comentario')
