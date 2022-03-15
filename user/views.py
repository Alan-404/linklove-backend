from django.http import JsonResponse
from rest_framework.decorators import api_view

from rest_framework.parsers import JSONParser

from user.dao import UserDAO

from common.lib import make_id

import base64
import PIL.Image as Image
import io
import os

from datetime import datetime

# Create your views here.


@api_view(['GET', 'POST'])
def user_api(request):
    if request.method == 'GET':
        try:
            data = UserDAO.get_all_users()
            return JsonResponse({'users': data}, status=200)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=500)
    elif request.method == 'POST':
        try:
            request_data = JSONParser().parse(request)
            handle_image = request_data['avatar'].split('base64,')[1]

            base = base64.b64decode(handle_image)
            img = Image.open(io.BytesIO(base))
            id = make_id()


            if os.path.exists(f'./common/images/users/{id}') == False:
                os.makedirs(f'./common/images/users/{id}')
            img = img.convert('RGB')
            img.save(f"./common/images/users/{id}/avatar.jpg")

            first_name = request_data['first_name']
            last_name = request_data['last_name']
            birth_date = request_data['birth_date']
            gender = request_data['gender']
            phone = request_data['phone']
            country = request_data['country']
            address = request_data['address']
            avatar = f"./common/images/users/{id}/avatar.jpg"
            email = request_data['email']
            password = request_data['password']
            if UserDAO.insert_user(id, first_name, last_name, birth_date, gender, phone, country, address, avatar, email, password) == True:
                return JsonResponse({'success': True}, status=200)
            return JsonResponse({"success": False}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, 'message': str(e)}, status=500)

@api_view(['GET'])
def auth_user(request):
    if request.method =='GET':
        try:
            authorization = request.headers.get('Authorization')
            user = UserDAO.get_user_token(authorization)
            if user:
                return JsonResponse({'user': user}, status=200)
            return JsonResponse({'message': "Invalid token"})
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)


@api_view(['GET'])
def info_user(request):
    if request.method =='GET':
        try:
            user = UserDAO.get_user_by_id(request.query_params['id'])
            return JsonResponse({'user': user}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
        
