from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin

from citybook.models import City
from citybook.serializers import CitySerializer, PlaceSerializer


class CityViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericViewSet):

    permission_classes = [AllowAny]
    serializer_class = CitySerializer
    queryset = City.objects.all()

    @action(detail=True, methods=["get"], url_path="places")
    def places(self, request, *args, **kwargs):
        city = self.get_object()
        self.queryset = city.places.all()
        self.serializer_class = PlaceSerializer
        return super().list(request, *args, **kwargs)   

