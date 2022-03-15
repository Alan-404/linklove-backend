from post_media.models import PostMediaModel
from post_media.serializers import PostMediaSerializer

from common.lib import convert_img_to_b64

class PostMediaDAO:
    def add_media(post_id, media):

        media_data = {
            'post_id': post_id,
            'media_link': media
        }

        media_serializer = PostMediaSerializer(data=media_data)
        if media_serializer.is_valid():
            media_serializer.save()
            return True
        return False
    
    def get_media_by_post(post_id):
        media = PostMediaModel.objects.filter(post_id=post_id)
        for item in list(media):
            item.media_link = convert_img_to_b64(item.media_link)
        media_serializer = PostMediaSerializer(media, many=True)
        return media_serializer.data