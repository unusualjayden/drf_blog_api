from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from users.views import TokenObtainPairView, UserPostsDetailView, registration

urlpatterns = [
    path('user/<username>/', UserPostsDetailView.as_view(), name='user-posts'),
    path('registration/', registration, name='registration'),
    path('auth/token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('auth/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),
]
