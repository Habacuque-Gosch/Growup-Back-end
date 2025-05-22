from rest_framework.permissions import BasePermission


class IsSuperuser(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            
            return False
        
        return True


class IsOwnerOrReadOnly(BasePermission):
    """
    Permite edição apenas se o usuário autenticado for o dono (owner) do objeto.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        return obj.user == request.user

