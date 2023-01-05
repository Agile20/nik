from rest_framework import serializers

from .models import *


class SparePartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpareParts
        fields = (
            'id', 'name', 'price', 'description', 'available',
        )


class PowerPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerPlant
        fields = (
            'id', 'name', 'price', 'description', 'available',
        )