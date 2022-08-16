
from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from posts.models import Comment, Follow, Group, Post
from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    """Передает объекты модели Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Передает объекты модели Comment."""

    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, IsAuthenticatedOrReadOnly)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        new_queryset = Comment.objects.filter(post=post)

        return new_queryset

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        current_post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=current_post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Передает объекты модели Group."""

    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class FollowList(ListCreateAPIView):
    """Передает объекты модели Follow."""

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        new_queryset = Follow.objects.filter(user=self.request.user)

        return new_queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
