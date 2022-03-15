from rest_framework import serializers
from user.models import UserModel

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class UserShowPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'first_name', 'last_name', 'avatar')