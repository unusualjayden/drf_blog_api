from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework import decorators, permissions, status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt import views as jwt_views
from rest_framework_simplejwt.tokens import RefreshToken

from posts.models import Post
from posts.serializers import UserPostSerializer
from users.serializers import UserActivitySerializer, UserCreateSerializer

User = get_user_model()


@decorators.api_view(['POST'])
@decorators.permission_classes([permissions.AllowAny])
def registration(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()
    refresh = RefreshToken.for_user(user)
    res = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return Response(res, status.HTTP_201_CREATED)


class TokenObtainPairView(jwt_views.TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        User.objects.filter(username=request.data.get('username')).update(last_login=timezone.now())
        return super(TokenObtainPairView, self).post(request, *args, **kwargs)


class UserPostsDetailView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    lookup_field = 'username'
    serializer_class = UserPostSerializer
    queryset = Post.objects.select_related('author')


class UserActivityView(ListAPIView):
    serializer_class = UserActivitySerializer
    queryset = User.objects.all().values('username', 'last_login', 'last_active')
    lookup_field = 'username'
