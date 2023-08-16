from django.contrib.auth.backends import BaseBackend
from yourapp.models import Users

class MatriculeBackend(BaseBackend):
    def authenticate(self, request, matricule=None, password=None, **kwargs):
        try:
            user = Users.objects.get(matricule=matricule)
        except Users.DoesNotExist:
            return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return Users.objects.get(pk=user_id)
        except Users.DoesNotExist:
            return None

