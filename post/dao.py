from post.models import PostModel
from post.serializers import PostSerializer

from account.dao import AccountDAO
from user.dao import UserDAO
from post_media.dao import PostMediaDAO

from datetime import datetime
from common.lib import make_big_id, convert_img_to_b64, convert_arr_b64_to_image


class PostDAO:
    def get_all_post():
        posts = PostModel.objects.all().order_by('created_at').reverse()
        users =[]
        for item in list(posts):
            user = UserDAO.get_user_by_id(item.user_id)
            #user['avatar'] = convert_img_to_b64(user['avatar'])
            users.append(user)
        posts_serializer = PostSerializer(posts, many=True)
        return (posts_serializer.data, users)

    def get_all_posts():
        posts = PostModel.objects.all().order_by('created_at').reverse()
        users =[]
        media = []
        for item in list(posts):
            user = UserDAO.get_user_by_id(item.user_id)
            post_media = PostMediaDAO.get_media_by_post(item.id)
            media.append(post_media)
            users.append(user)
        posts_serializer = PostSerializer(posts, many=True)
        return (posts_serializer.data, users, media)

    def add_post(authorization, content):
        user_id = AccountDAO.get_user_id_token(authorization)
        if user_id is None:
            return False
        post_data = {
            'id': make_big_id(),
            'content': content,
            'user_id': user_id,
            'created_at': datetime.now(),
            'modified_at': datetime.now()
        }
        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return True
        return False

    def insert_post(authorization, content, media):
        user_id = AccountDAO.get_user_id_token(authorization)
        if user_id is None:
            return False
        post_id = make_big_id()
        post_data = {
            'id': post_id,
            'content': content,
            'user_id': user_id,
            'created_at': datetime.now(),
            'modified_at': datetime.now()
        }
        

        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            for index, item in enumerate(media):
                path = convert_arr_b64_to_image(item, post_id, index)
                PostMediaDAO.add_media(post_id, path)
            return True
        return False

    def get_posts_by_user(user_id):
        posts = PostModel.objects.filter(user_id=user_id).order_by('created_at').reverse()
        posts_serializer = PostSerializer(posts, many=True)
        return (posts_serializer.data)