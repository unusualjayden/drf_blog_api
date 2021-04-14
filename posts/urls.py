from django.urls import include, path
from rest_framework import routers

from .views import AnalyticsView, PostViewSet, post_like

router = routers.DefaultRouter(trailing_slash=True)
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
    path('post/<post_id>/like/', post_like, name='post-like'),
]
