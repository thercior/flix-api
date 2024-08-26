from rest_framework import serializers
from atores.models import Ator


class AtorSerializer(serializers.ModelSerializer):
    nacionalidade = serializers.SerializerMethodField

    class Meta:
        model = Ator
        fields = '__all__'

    def get_nacionalidade(self, obj):
        return obj.get_nacionalidade_display()
