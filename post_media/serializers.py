from rest_framework import serializers
from post_media.models import PostMediaModel

class PostMediaSerializer (serializers.ModelSerializer):
    class Meta:
        model = PostMediaModel
        fields = '__all__'