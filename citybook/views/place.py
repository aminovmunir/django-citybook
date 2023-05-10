from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin

from citybook.models import Place
from citybook.serializers import PlaceSerializer


class PlaceViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = PlaceSerializer

    def get_queryset(self):
        queryset = Place.objects.all()
        search_name = self.request.query_params.get('name', None)
        search_address = self.request.query_params.get('address', None)

        if search_name is not None:
            queryset = queryset.filter(name__icontains=search_name.lower())
        if search_address is not None:
            queryset = queryset.filter(address__icontains= search_address.lower())
        return queryset
