from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.parsers import JSONParser

from hobby.dao import HobbyDAO

# Create your views here.


@api_view(['GET', 'POST'])
def hobby_api(request):
    if request.method == 'GET':
        try:
            hobbies = HobbyDAO.get_all_hobbies()
            return JsonResponse({'hobbies':hobbies}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    elif request.method == 'POST':
        try:
            request_data = JSONParser().parse(request)
            if HobbyDAO.add_hobby(request_data['name'], request_data['image']):
                return JsonResponse({'success': True}, status=200)
            return JsonResponse({"success": False}, status=400)
        except Exception as e:
            return JsonResponse({'success': False}, status=500)