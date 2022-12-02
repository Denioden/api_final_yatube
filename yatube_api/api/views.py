from django.shortcuts import get_object_or_404

from posts.models import Post, Group, Comment, Follow
from .serializers import PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import AuthorOrReadOnly, ReadOnly
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.request.method == 'GET':
            return (ReadOnly(),)
        return super().get_permissions()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    def get_permissions(self):
        if self.request.method == 'GET':
            return (ReadOnly(),)
        return super().get_permissions()
    
    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)
 
    def get_queryset(self):
        return self.request.user.follower.all()
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)