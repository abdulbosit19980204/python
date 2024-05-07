from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        pass

    def has_permission(self, request, view):
        pass


class IsSuperAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return False

    def has_permission(request, view):
        if not request.user.is_authenticated:
            return True
        return False
