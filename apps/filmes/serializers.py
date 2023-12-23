from django.db.models import Avg
from rest_framework import serializers
from filmes.models import Filme

class FilmeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Filme
        fields = '__all__'
    
    # def get_rate(self, obj):
    #     average_rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        
    #     if average_rate:
    #         return round(average_rate, 1)
    
    def validate_resumo(self, value):
        if len(value) > 200:
            raise serializers.ValidationError('O campo resumo não pode ser maior que  200 caracteres')
        return value
    