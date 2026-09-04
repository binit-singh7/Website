from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Activity, ActivityCategory
from .serializers import (
    ActivityCategorySerializer,
    ActivityDetailSerializer,
    ActivityListSerializer,
)


class ActivityCategoryListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ActivityCategorySerializer
    pagination_class = None
    queryset = ActivityCategory.objects.all()


class ActivityListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ActivityListSerializer

    def get_queryset(self):
        queryset = Activity.objects.filter(
            status=Activity.STATUS_PUBLISHED
        ).select_related("category")
        category = self.request.query_params.get("category")
        year = self.request.query_params.get("year")
        featured = self.request.query_params.get("featured")

        if category:
            queryset = queryset.filter(category__slug=category)
        if year and year.isdigit():
            queryset = queryset.filter(date__year=year)
        if featured in {"true", "false"}:
            queryset = queryset.filter(featured=featured == "true")
        return queryset


class ActivityDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ActivityDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return (
            Activity.objects.filter(status=Activity.STATUS_PUBLISHED)
            .select_related("category")
            .prefetch_related("images")
        )
