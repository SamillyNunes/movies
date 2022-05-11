from rest_framework import serializers

from .models import PersonModel, MovieModel, AddressModel


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MovieModel
        fields = ('id', 'title', 'duration', 'gender', 'isAvailable')


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AddressModel
        fields = ('id', 'street', 'zipCode', 'number', 'neighborhood', 'city', 'state', 'country')


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonModel
        fields = ('id', 'name', 'date_of_birth', 'cpf', 'address', 'located_movies', 'has_debits')