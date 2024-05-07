from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.id != obj.author.id:
            return False
        return True

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return True
