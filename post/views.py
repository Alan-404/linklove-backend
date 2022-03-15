from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from post.dao import PostDAO
# Create your views here.


@api_view(['GET', 'POST'])
def post_api(request):
    if request.method == 'GET':
        try:
            (posts, users) = PostDAO.get_all_post()
            return JsonResponse({'posts': posts, 'users': users}, status=200)
        except Exception as e:
            return JsonResponse({'message': str(e)}, status=500)
    elif request.method == 'POST':
        try:
            request_data = JSONParser().parse(request)
            authorization = request.headers.get('Authorization')
            content = request_data['content']
            if PostDAO.add_post(authorization, content):
                return JsonResponse({'success': True}, status=200)
            return JsonResponse({'success': False}, status=400)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)


@api_view(['GET'])
def posts_user(request):
    if request.method == 'GET':
        try:
            posts = PostDAO.get_posts_by_user(request.query_params['id'])
            return JsonResponse({'posts': posts}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@api_view(['POST'])
def post(request):
    if request.method == 'POST':
        try:
            request_data = JSONParser().parse(request)
            print(request.headers.get('Authorization'))
            if PostDAO.insert_post(request.headers.get('Authorization'), request_data['post']['content'], request_data['media']) == True:
                return JsonResponse({'success': True}, status=200)
            return JsonResponse({"success": False}, status=400)
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)}, status=500)

@api_view(['GET'])
def get_posts(request):
    if request.method == 'GET':
        try:
            (posts, users, media) = PostDAO.get_all_posts()
            return JsonResponse({'posts': posts, 'users': users, 'media': media}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)