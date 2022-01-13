from rest_framework import generics
from .serializers import WorkSpaceDetailSerializer, WorkSpaceListSerializer
from .models import WorkSpace
from booking.models import Booking
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from .utils import is_datetime_valid
from rest_framework.exceptions import ValidationError
from dateutil import parser


class WorkSpaceCreateView(generics.CreateAPIView):
    serializer_class = WorkSpaceDetailSerializer
    permission_classes = (IsAuthenticated,)


class WorkSpaceListView(generics.ListAPIView):
    serializer_class = WorkSpaceListSerializer
    queryset = WorkSpace.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        beginning = self.request.query_params.get('datetime_from')
        ending = self.request.query_params.get('datetime_to')
        return self.get_free_workspaces_in_range(beginning, ending)

    def get_free_workspaces_in_range(self, beginning, ending):
        bookings = Booking.objects.all()
        workspace_ids = Booking.objects.all().values_list('workspace')

        if beginning and ending:
            if is_datetime_valid(beginning) and is_datetime_valid(ending):
                beginning_datetime = parser.parse(beginning)
                ending_datetime = parser.parse(ending)
                workspace_ids = bookings.exclude(
                    beginning__range=[beginning_datetime, ending_datetime]).exclude(
                    ending__range=[beginning_datetime, ending_datetime]).values_list('workspace', flat=True)
            else:
                raise ValidationError
        elif beginning and not ending:
            if is_datetime_valid(beginning):
                beginning_datetime = parser.parse(beginning)
                workspace_ids = Booking.objects.filter(
                    ending__lt=beginning_datetime
                ).values_list('workspace', flat=True)
            else:
                raise ValidationError
        elif ending and not beginning:
            if is_datetime_valid(ending):
                ending_datetime = parser.parse(ending)
                workspace_ids = Booking.objects.filter(
                    beginning__gt=ending_datetime
                ).values_list('workspace', flat=True)
            else:
                raise ValidationError
        return WorkSpace.objects.filter(id__in=workspace_ids)


class WorkSpaceDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = WorkSpaceDetailSerializer
    queryset = WorkSpace.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
