from rest_framework import serializers
from rest_framework.filters import SearchFilter

from citybook.models import Place
from citybook.serializers import CitySerializer, CategorySerializer, ContactSerializer

class PlaceSerializer(serializers.ModelSerializer):

    city = CitySerializer()
    category = CategorySerializer()
    contacts = ContactSerializer()
    filter_backends = [SearchFilter]
    search_fields = ['address', 'city__name']

    class Meta:
        model = Place
        fields = "__all__"