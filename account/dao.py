from account.models import AccountModel
from account.serializers import AccountSerializer

from common.lib import make_id
import jwt

from common.secret import key_token

from datetime import datetime

from django.contrib.auth.hashers import make_password, check_password

class AccountDAO:


    def insert_account(user_id, email, password):
        if email is None or password is None or user_id is None:
            return False
        account_data = {
            'id': make_id(),
            'user_id': user_id,
            'email': email,
            'password': make_password(password)
        }
        account_serializer = AccountSerializer(data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return True
        return False

    def login_account(email, password):
        account = AccountModel.objects.filter(email=email).first()
        if account is None:
            return False
        if check_password(password, account.password):
            payload = {
                'id': account.id,
                'created_at': str(datetime.now())
            }
            return jwt.encode(payload, key_token, algorithm='HS256')
        return False

    def get_user_id_token(authorization):
        token = authorization.split(' ')[1]
        
        if token is None:
            return False
        account_id = jwt.decode(token, key_token, algorithms='HS256')['id']
        user_id = AccountModel.objects.filter(id=account_id).first().user_id
        return user_id

    
