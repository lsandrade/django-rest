from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it
    """

    def has_object_permission(self, request, view, obj):
        # read permission are allowed to any request
        # so we'll always allow GET, HEAD or OPTIONS request
        if request.method in permissions.SAFE_METHODS:
            return True

        # write permissions are only allowed to the oener of the snippet
        return obj.owner == request.user