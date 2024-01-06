from rest_framework import permissions

class GeneroPermissions(permissions.BasePermission):
    
    def has_permission(self, request, view):
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('generos.view_genero')
        
        if request.method == 'POST':
            return request.user.has_perm('generos.add_genero')
        
        return False