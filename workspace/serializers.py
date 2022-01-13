from rest_framework import serializers
from .models import WorkSpace


class WorkSpaceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkSpace
        fields = ('id', 'name', 'type', 'city_location', 'address')


class WorkSpaceDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = WorkSpace
        fields = '__all__'
