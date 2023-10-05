
from rest_framework import viewsets
from .serializers import (
    UserSerializer,
    UserCreateSerializer
)

from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets > ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.get_serializer().Meta.model.objects.filter(is_active=True)
            return self.queryset
        else:
            return self.queryset

    def get_object(self, pk):
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk)
