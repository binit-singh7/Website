from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Event
from .serializers import EventDetailSerializer, EventSerializer


class EventListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = Event.objects.exclude(status=Event.STATUS_DRAFT)
        status = self.request.query_params.get("status")
        year = self.request.query_params.get("year")
        featured = self.request.query_params.get("featured")

        if status:
            queryset = queryset.filter(status=status)
        if year and year.isdigit():
            queryset = queryset.filter(start_datetime__year=year)
        if featured in {"true", "false"}:
            queryset = queryset.filter(featured=featured == "true")
        if status in {Event.STATUS_COMPLETED, Event.STATUS_CANCELLED}:
            return queryset.order_by("-start_datetime")
        return queryset.order_by("start_datetime")


class EventDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = EventDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return Event.objects.exclude(status=Event.STATUS_DRAFT).prefetch_related(
            "images"
        )
