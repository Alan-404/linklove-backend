from rest_framework import serializers
from friend_request.models import FriendRequestModel


class FriendRequestSerializer (serializers.ModelSerializer):
    class Meta:
        model = FriendRequestModel
        fields = '__all__'