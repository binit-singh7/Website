from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Announcement, Organization
from .serializers import AnnouncementSerializer, OrganizationSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def health_check(request):
    """Return the backend availability status for local and deployment checks."""
    return Response({"status": "ok"})


class OrganizationView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = OrganizationSerializer

    def get_object(self):
        return get_object_or_404(Organization.objects.order_by("id"))


class AnnouncementListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = AnnouncementSerializer
    pagination_class = None

    def get_queryset(self):
        today = timezone.localdate()
        return Announcement.objects.filter(is_active=True).filter(
            Q(start_date__isnull=True) | Q(start_date__lte=today),
            Q(end_date__isnull=True) | Q(end_date__gte=today),
        )

def health_check(request):
    return JsonResponse({"status": "ok"}, status=200)