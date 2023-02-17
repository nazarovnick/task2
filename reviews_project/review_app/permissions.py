from rest_framework import permissions

class HasTokenOrReadAndCreate(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in ('GET', 'POST', 'HEAD', 'OPTIONS'):
            return True

        return bool(request.user and request.user.is_staff)

    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'POST', 'HEAD', 'OPTIONS'):
            return True

        return bool(request.user and request.user.is_staff)

