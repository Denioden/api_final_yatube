from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.shortcuts import get_object_or_404

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
        read_only_fields = ('id',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    following = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field='username'
    )

    def validate(self, data):
        following = get_object_or_404(User, username=data['following'])
        follow = Follow.objects.filter(
            user=self.context['request'].user, following=following
        ).exists()

        if following == self.context['request'].user:
            raise serializers.ValidationError(
                "Вы не можете подписаться на самого себя"
            )
        if follow:
            raise serializers.ValidationError(
                "Вы уже подписаны на пользователя"
            )
        return data

    class Meta:
        fields = '__all__'
        model = Follow
