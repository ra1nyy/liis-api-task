from rest_framework import serializers
from .models import Booking
from workspace.models import WorkSpace


class BookingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('user', 'workspace', 'beginning', 'ending')


class BookingDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Booking
        fields = '__all__'
