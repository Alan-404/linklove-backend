from hobby.models import HobbyModel
from hobby.serializers import HobbySerializer

from common.lib import convert_img_to_b64

class HobbyDAO:

    def get_all_hobbies():
        hobbies = HobbyModel.objects.all()
        for item in list(hobbies):
            item.image = convert_img_to_b64(item.image)
        hobbies_serializer = HobbySerializer(hobbies, many=True)
        return hobbies_serializer.data

    def add_hobby(name, image):
        hobby_data = {
            'name': name,
            'image': image
        }
        hobby_serializer = HobbySerializer(data=hobby_data)
        if hobby_serializer.is_valid():
            hobby_serializer.save()
            return True
        return False