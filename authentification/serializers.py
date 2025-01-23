from rest_framework.serializers import ModelSerializer

from .models import User

class UserSerializer(ModelSerializer):
    class Meta:
       model = User
       fields = ['pk','username','last_name', 'first_name', 'password']