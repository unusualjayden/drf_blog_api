from rest_framework import serializers

from posts.models import Post


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body')
