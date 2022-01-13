from rest_framework import generics
from .serializers import BookingDetailSerializer, BookingListSerializer
from .models import Booking
from django_filters.rest_framework import DjangoFilterBackend


class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingDetailSerializer


class BookingListView(generics.ListAPIView):
    serializer_class = BookingListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('workspace',)
    queryset = Booking.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Booking.objects.filter(user=user)
        return None


class BookingDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookingDetailSerializer
    queryset = Booking.objects.all()
