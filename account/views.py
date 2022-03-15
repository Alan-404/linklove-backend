from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http import JsonResponse

from account.dao import AccountDAO
# Create your views here.


@api_view(['GET', 'POST'])
def auth_account(request):
    if request.method == 'POST':
        try:
            request_data = JSONParser().parse(request)
            email = request_data['email']
            password = request_data['password']
            access_token = AccountDAO.login_account(email, password)
            if access_token:
                return JsonResponse({'success': True, "access_token": access_token}, status=200)
            return JsonResponse({'success': False}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)
        
