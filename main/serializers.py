from rest_framework import serializers

from .models import *


class MainPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPicture
        fields = (
            'id', 'image',
        )


class MainCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCatalog
        fields = (
            'id', 'category',
        )


class MainAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = (
            'id', 'title', 'description',
        )


class MainConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Connection
        fields = (
            'id', 'number', 'adress', 'email', 'social_network',
        )
        read_only_fields = ('number', 'adress', 'email',)


