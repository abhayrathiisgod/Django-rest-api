from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
#from .models import student

#getting the content type

content_type = ContentType.objects.get_for_model(student)
permission = Permission.objects.get(content_type= content_type, codename='can_edit_student_grade')


user = User.objects.get(username='abhayrathi')

user.user_permissions.add(permission)

