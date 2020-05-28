from rest_framework import serializers
from core.models import Desejos, Item

class DesejosSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Desejos
        fields = ['id', 'nomeUser', 'nomeLista', 'url', 'email', 'percent']


class ItemSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Item
        fields = ['id', 'lista', 'title', 'minPrice', 'dateCreated', 'priceDayAdd']