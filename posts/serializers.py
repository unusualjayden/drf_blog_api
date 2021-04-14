from rest_framework import serializers

from posts.models import Post


class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'body')


class AnalyticsSerializer(serializers.Serializer):
    created_at__date = serializers.DateField()
    post = serializers.IntegerField()
    likes = serializers.IntegerField()

    def to_representation(self, instance):
        return {
            'date': instance.get('created_at__date'),
            'post': instance.get('post'),
            'likes': instance.get('likes')
        }
