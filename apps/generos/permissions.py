from rest_framework import permissions

class GeneroPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        
        return True