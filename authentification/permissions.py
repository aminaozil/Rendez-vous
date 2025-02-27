
from rest_framework import permissions

class IsStaffPermision(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return super().has_permission(request, view)
    
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }