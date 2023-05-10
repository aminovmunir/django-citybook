from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, CreateModelMixin

from citybook.models import Category
from citybook.serializers import CategorySerializer, PlaceSerializer


class CategoryViewSet(ListModelMixin, RetrieveModelMixin, CreateModelMixin, GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    @action(detail=True, methods=["get"], url_path="places")
    def places(self, request, *args, **kwargs):
        category = self.get_object()
        self.queryset = category.places.all()
        self.serializer_class = PlaceSerializer
        return super().list(request, *args, **kwargs)