from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import decorators, permissions, status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from posts.models import Like, Post
from posts.serializers import AnalyticsSerializer, UserPostSerializer
from posts.services import analytics_prettify_data, parse_analytics_date


class PostViewSet(ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Post.objects.all().select_related('author')
    serializer_class = UserPostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.IsAuthenticated])
def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    try:
        Like.objects.get(user=request.user, post=post).delete()
        return Response({'response': 'unliked'}, status.HTTP_200_OK)
    except Like.DoesNotExist:
        Like.objects.create(user=request.user, post=post)
    return Response({'response': 'liked'}, status.HTTP_201_CREATED)


class AnalyticsView(ListAPIView):
    serializer_class = AnalyticsSerializer

    def get_queryset(self):
        dates = parse_analytics_date(request=self.request)
        return Like.objects.filter(**dates).values('created_at__date', 'post').order_by('-created_at__date').annotate(
            likes=Count('post'))

    def list(self, request, *args, **kwargs):
        raw_data = list(super(AnalyticsView, self).list(request, *args, **kwargs).data)
        return Response(analytics_prettify_data(raw_data))
