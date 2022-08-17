
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from posts.models import Comment, Group, Post
from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from .viewset_mixins import ListCreateViewSet

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """Передает объекты модели Post."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    """Передает объекты модели Comment."""

    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)

        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        current_post = get_object_or_404(Post, id=post_id)
        serializer.save(author=self.request.user, post=current_post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Передает объекты модели Group."""

    serializer_class = GroupSerializer
    queryset = Group.objects.all()


class FollowViewSet(ListCreateViewSet):
    """Передает объекты модели Follow."""

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=following__username', '=user__username')

    def get_queryset(self):
        user = self.request.user

        return user.followwer.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
