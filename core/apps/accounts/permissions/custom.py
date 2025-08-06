from rest_framework.permissions import BasePermission

class IsAuthenticatedUser(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        print(request.user.is_authenticated)
        return request.user and request.user.is_authenticated
