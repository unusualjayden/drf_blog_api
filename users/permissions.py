from rest_framework import permissions
from posts.models import Post


class IsAuthor(permissions.BasePermission):
    """
    Check if user is post author or not.
    """
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
