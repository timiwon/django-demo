from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import AbstractUser

class UserTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user: AbstractUser):
        token = super().get_token(user)

        # Add custom claims
        token['is_staff'] = user.is_staff
        token['permissions']= list(user.get_all_permissions())

        return token