from rest_framework import serializers
from hobby.models import HobbyModel
class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model = HobbyModel
        fields = '__all__'