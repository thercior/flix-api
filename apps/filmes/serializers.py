from django.db.models import Avg
from rest_framework import serializers
from atores.serializers import AtorSerializer
from generos.serializers import GeneroSerializer
from filmes.models import Filme


class FilmeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Filme
        fields = '__all__'

    def validate_resumo(self, value):
        if len(value) > 1000:
            raise serializers.ValidationError('O campo resumo não pode ser maior que 1000 caracteres')
        return value


class FilmeListDetailSerializer(serializers.ModelSerializer):
    atores = AtorSerializer(many=True)  # vários atores - uma lista de atores, por isso Many = True
    genero = GeneroSerializer()  # só vem um dado, logo o padrão Many = False
    avaliacao = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Filme
        fields = ['id', 'titulo', 'genero', 'atores', 'ano', 'avaliacao', 'resumo']

    def get_avaliacao(self, obj):
        average_avaliacao = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if average_avaliacao:
            return round(average_avaliacao, 1)


class FilmeStatisticsSerializer(serializers.Serializer):
    total_filmes = serializers.IntegerField()
    filmes_por_genero = serializers.ListField()
    total_reviews = serializers.IntegerField()
    media_avaliacoes = serializers.FloatField()
