from rest_framework import generics
from rest_framework.permissions import AllowAny

from activities.models import Activity
from .models import GalleryAlbum
from .serializers import (
    ActivityAsAlbumDetailSerializer,
    ActivityAsAlbumSerializer,
    GalleryAlbumDetailSerializer,
    GalleryAlbumSerializer,
)


class GalleryAlbumListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = GalleryAlbumSerializer
    queryset = GalleryAlbum.objects.filter(is_published=True)


class GalleryAlbumDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = GalleryAlbumDetailSerializer
    lookup_field = "slug"
    queryset = GalleryAlbum.objects.filter(is_published=True).prefetch_related("images")


# ---------------------------------------------------------------------------
# Activity images surfaced as virtual gallery albums.
#
# These views dynamically derive their data from published Activity records.
# No Gallery database records are created; the Activity model is the single
# source of truth for both the Activities section and this gallery feed.
# ---------------------------------------------------------------------------

def _activity_gallery_queryset():
    """
    Return published Activities that have at least one image to show:
    either a cover_image or one or more ActivityImage detail records.
    Prefetch images for efficient access.
    """
    from django.db.models import Q, Count
    return (
        Activity.objects
        .filter(status=Activity.STATUS_PUBLISHED)
        .prefetch_related("images")
        .annotate(_image_count=Count("images"))
        .filter(
            Q(cover_image__isnull=False, cover_image__gt="") | Q(_image_count__gt=0)
        )
        .select_related("category")
        .order_by("-date")
    )


class ActivityGalleryListView(generics.ListAPIView):
    """
    List published Activities shaped as gallery albums.

    GET /api/gallery/activity-images/

    Returns the same paginated envelope as the GalleryAlbumListView so the
    frontend can merge both feeds without special-casing the response shape.
    Each item includes a ``source: "activity"`` field and a slug prefixed
    with ``activity--`` so the frontend can route detail requests correctly.
    """
    permission_classes = [AllowAny]
    serializer_class = ActivityAsAlbumSerializer

    def get_queryset(self):
        return _activity_gallery_queryset()


class ActivityGalleryDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single published Activity shaped as a gallery album detail.

    GET /api/gallery/activity-images/<slug>/

    The <slug> here is the plain Activity slug (without the ``activity--``
    prefix the list view adds). The response includes an ``images[]`` array
    built from ActivityImage records, with the cover_image prepended when it
    is not already present in that set. No files are copied or duplicated.
    """
    permission_classes = [AllowAny]
    serializer_class = ActivityAsAlbumDetailSerializer
    lookup_field = "slug"

    def get_queryset(self):
        return _activity_gallery_queryset()
