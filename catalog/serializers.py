from rest_framework import serializers

from .models import *


class CatalogCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'id', 'name', 'available', 'torque', 'max_speed', 'type_kuz', 'type_priv', 'mileage', 'year_release', 'battery_capacity', 'price', 'description',
        )


class CatalogBikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = (
            'id', 'name', 'available', 'torque', 'max_speed', 'mileage', 'year_release', 'battery_capacity', 'price', 'description',
        )


class CatalogOtherTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherTransport
        fields = (
            'id', 'name', 'available', 'torque', 'max_speed', 'mileage', 'year_release', 'battery_capacity', 'price', 'description',
        )