from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):

    def has_permission(self, request, view):
        if not request.user.is_staff:
            return False
        
        return super().has_permission(request, view)
    '''
    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions())
        if  request.user.is_staff:
            if user.has.perm("product.view_product"): #app_name.verb_model_name
                return True
            if user.has.perm("product.add_product"):
                return True
            if user.has.perm("product.change_product"):
                return True
            if user.has.perm("product.delete_product"):
                return True
            return False
        return False
        '''