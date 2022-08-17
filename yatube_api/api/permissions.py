from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Дает право на чтение всем пользователям.

    Дает право на изменение/удаление объекта только его автору.
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
