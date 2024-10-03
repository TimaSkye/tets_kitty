from rest_framework import serializers

from .models import Breed, Kitten


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class KittenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitten
        fields = '__all__'
        read_only_fields = ['owner']


class KittenRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kitten
        fields = ['rating']
