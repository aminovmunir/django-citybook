from django.urls import path, include
from rest_framework import routers

from citybook.views import PlaceViewSet, CityViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register("places", PlaceViewSet, "places")
router.register("cities", CityViewSet, "cities")
router.register("categories", CategoryViewSet, "categories")


urlpatterns = [
    path('', include(router.urls)),
]