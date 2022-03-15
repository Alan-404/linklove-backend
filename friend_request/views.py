from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from friend_request.dao import FriendRequestDAO

# Create your views here.

@api_view(['POST'])
def friend_request_api(request):
    if request.method == 'POST':
        try:
            request_data = JSONParser().parse(request)
            if FriendRequestDAO.send_request(request.headers.get('Authorization'), request_data['to']) == True:
                return JsonResponse({'success': True}, status=200)
            return JsonResponse({'success': False}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)},status=500)

@api_view(['GET', 'POST'])
def request_handle(request):
    if request.method == 'GET':
        try:
            (all_requests, users) = FriendRequestDAO.get_all_requests(request.headers.get('Authorization'))
            return JsonResponse({'requests': all_requests, 'users': users}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    elif request.method == 'POST':
        try:
            request_data = JSONParser().parse(request)
            if request_data['id'] is None:
                return JsonResponse({"success": False}, status=400)
            if FriendRequestDAO.accept_friend_request(request.headers.get('Authorization'), request_data['id']):
                return JsonResponse({'success': True}, status=200)
            return JsonResponse({"success": False}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=500)
