from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Breed, Kitten
from .serializers import BreedSerializer, KittenSerializer, KittenRatingSerializer


class BreedViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class KittenViewSet(viewsets.ModelViewSet):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [permissions.IsAuthenticated]

    # authentication_classes = [authentication.JWTAuthentication]

    def get_queryset(self):
        if self.action == 'list':
            return Kitten.objects.filter(owner=self.request.user)
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.owner != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        super().perform_destroy(instance)

    @action(methods=['get'], detail=True)
    def by_breed(self, request, pk=None):
        breed = self.get_object().breed
        kittens = Kitten.objects.filter(breed=breed)
        serializer = self.get_serializer(kittens, many=True)
        return Response(serializer.data)

    @action(methods=['patch'], detail=True)
    def rate(self, request, pk=None):
        kitten = self.get_object()
        serializer = KittenRatingSerializer(kitten, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
