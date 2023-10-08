from .serializers import (
    PostSerializer,
    PostCreateSerializer
)

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from apps.user.models import CustomPagination


class PostViewSet(viewsets.ModeViewSet):
    serializer_class = PostSerializer

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = Post.objects.all()
            return self.queryset
        else:
            return self.queryset

    def get_object(self, pk=None):
        return get_object_or_404(Post, pk=pk)

    def list(self, request):
        posts = self.serializer_class.Meta.model.objects.order_by('-id').all()
        paginator = CustomPagination()
