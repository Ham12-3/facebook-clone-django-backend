from .serializers import (
    PostSerializer,
    PostCreateSerializer
)

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from apps.user.models import CustomPagination


def is_owner(request, instance):
    return request.user == instance.author or request.user.is_staff  # boolean value


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
        results = paginator.paginate_queryset(posts, request)

        post_serializers = self.get_serializer(results, many=True)
        return paginator.get_paginated_response(post_serializers.data)

    def create(self, request):
        post_serializer = PostCreateSerializer(data=request.data)
        if post_serializer.is_valid():
            post_serializer.save()
            return Response(post_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        posts = self.get_object(pk=pk)
        post_serializer = self.serializer_class(posts)
        return Response(post_serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        post = self.get_object(pk=pk)
        if not is_owner(request, post):
            return Response({'message': 'You are not authorized to perform this action'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            if 'image' not in request.data or request.data['image'] == '':
                data = request.data.copy()
                current_image = post.image
                data['image'] = current_image

                post_serializer = PostSerializer(post, data=data)
                if post_serializer.is_valid():
                    return Response({'message': 'Post updated successfully'}, status=status.HTTP_200_OK)
