from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsActiveUser(BasePermission):
    """
    Permissão que bloqueia qualquer requisição de usuários inativos.
    """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if not request.user.is_active:
            raise PermissionDenied("Sua conta está desativada.")
        return True
