from rest_framework import permissions

class isAdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        return super().has_permission(request, view) or request.method == 'GET'
    
class ReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user