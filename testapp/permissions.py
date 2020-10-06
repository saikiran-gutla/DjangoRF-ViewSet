from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsReadOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False


class SpecificPermission(BasePermission):
    def has_permission(self, request, view):
        username = request.user.username
        if username.lower() == "sai":
            return True
        elif username != "" and len(username) > 10 and request.method in ['GET']:
            return True
        else:
            return False
