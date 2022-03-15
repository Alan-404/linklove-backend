import base64
from user.models import UserModel
from user.serializers import UserSerializer, UserShowPostSerializer

from common.lib import make_id

from datetime import datetime

from account.dao import AccountDAO

from PIL import Image
from common.lib import convert_img_to_b64

class UserDAO:
    def get_all_users():
        users = UserModel.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return users_serializer.data

    def insert_user(id, first_name, last_name, birth_date, gender, phone ,country, address, avatar, email, password):
        #print(avatar)

        if first_name is None or last_name is None or phone is None:
            return False
        user_data = {
            'id': id,
            'first_name': first_name,
            'last_name': last_name,
            'birth_date': birth_date,
            'gender': gender,
            'phone': phone,
            'country': country,
            'address': address,
            'avatar': avatar,
            'created_at': datetime.now(),
            'modified_at': datetime.now()
        }
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            if AccountDAO.insert_account(user_data['id'], email, password) == True:
                return True
        return False 

    def get_user_token(authorization):
        user_id = AccountDAO.get_user_id_token(authorization)
        if user_id is None:
            return False
        user = UserModel.objects.filter(id=user_id).first()
        with open(user.avatar, "rb") as img_file:
            str_64 = base64.b64encode(img_file.read())
        user.avatar = "data:image/jpeg;base64," +  str(str_64)[2:-1]

        user_serializer = UserSerializer(user)
        return user_serializer.data
    
    def get_user_by_id(user_id):
        user = UserModel.objects.filter(id=user_id).first()
        user.avatar = convert_img_to_b64(user.avatar)
        user_serializer = UserSerializer(user)
        return user_serializer.data
        