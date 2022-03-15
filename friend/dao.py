from friend.models import FriendModel
from friend.serializers import FriendSerializer

from datetime import datetime


class FriendDAO:
    def make_friend(user_1, user_2):
        friend1_data = {
            'user_id': user_1,
            'friend_id': user_2,
            'created_at': datetime.now()
        }

        friend2_data = {
            'user_id': user_2,
            'friend_id': user_1,
            'created_at': datetime.now()
        }

        friend_1_serializer = FriendSerializer(data=friend1_data)
        if friend_1_serializer.is_valid():
            friend_1_serializer.save()
            friend_2_serializer = FriendSerializer(data=friend2_data)
            if friend_2_serializer.is_valid():
                friend_2_serializer.save()
                return True
        return False

    def get_all_friends(user_id):
        friends = FriendModel.objects.filter(user_id=user_id)
        friends_serializer = FriendSerializer(friends, many=True)
        return friends_serializer.data
