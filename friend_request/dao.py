from friend_request.models import FriendRequestModel
from friend_request.serializers import FriendRequestSerializer

from account.dao import AccountDAO

from user.dao import UserDAO
from friend.dao import FriendDAO
from datetime import datetime

class FriendRequestDAO:
    def send_request(authorization, to):
        user_id = AccountDAO.get_user_id_token(authorization)
        if user_id is None:
            return False
        request_data = {
            'request_from': user_id,
            'request_to': to,
            'created_at': datetime.now()
        }

        request_serializer = FriendRequestSerializer(data=request_data)
        if request_serializer.is_valid():
            request_serializer.save()
            return True
        return False

    def get_all_requests(authorization):
        user_id = AccountDAO.get_user_id_token(authorization)
        if user_id is None:
            return False
        all_requests = FriendRequestModel.objects.filter(request_to=user_id)
        users = []
        for request in list(all_requests):
            users.append(UserDAO.get_user_by_id(request.request_from))
        request_serializer = FriendRequestSerializer(all_requests, many=True)
        return (request_serializer.data, users)


    def accept_friend_request(authorization, request_id):
        user_id = AccountDAO.get_user_id_token(authorization)
        request_from = FriendRequestModel.objects.filter(id=request_id).first()
        if request_from.request_to != user_id:
            return False
        if user_id is None:
            return False
        if FriendDAO.make_friend(user_id, request_from.request_from):
            request = FriendRequestModel.objects.filter(id = request_id)
            if request is None:
                return False
            request.delete()
            return True
        return False
