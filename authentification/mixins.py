from .permissions import IsStaffPermision
from rest_framework import permissions

class StaffPermissionsMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffPermision]
