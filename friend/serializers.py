from rest_framework import serializers
from friend.models import FriendModel

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendModel
        fields = '__all__'