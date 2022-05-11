from django.shortcuts import render

from rest_framework import viewsets

from .serializers import MovieSerializer, PersonSerializer, AddressSerializer
from .models import MovieModel, AddressModel, PersonModel


class MovieViewset(viewsets.ModelViewSet):
    queryset = MovieModel.objects.all().order_by('title')
    serializer_class = MovieSerializer


class PersonViewset(viewsets.ModelViewSet):
    queryset = PersonModel.objects.all().order_by('name')
    serializer_class = PersonSerializer


class AddressViewset(viewsets.ModelViewSet):
    queryset = AddressModel.objects.all().order_by('city')
    serializer_class = AddressSerializer
