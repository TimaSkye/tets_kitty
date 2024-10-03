from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import BreedViewSet, KittenViewSet

router = DefaultRouter()
router.register('breeds', BreedViewSet)
router.register('kittens', KittenViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
