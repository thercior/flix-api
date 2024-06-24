from rest_framework import serializers
from filmes.serializers import FilmeSerializer
from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'


class ReviewListDetailSerializer(serializers.ModelSerializer):
    filme = FilmeSerializer()

    class Meta:
        model = Review
        fields = ['id', 'filme', 'stars', 'comentario']
