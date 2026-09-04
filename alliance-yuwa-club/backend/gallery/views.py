from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import GalleryAlbum
from .serializers import GalleryAlbumDetailSerializer, GalleryAlbumSerializer


class GalleryAlbumListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = GalleryAlbumSerializer
    queryset = GalleryAlbum.objects.filter(is_published=True)


class GalleryAlbumDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = GalleryAlbumDetailSerializer
    lookup_field = "slug"
    queryset = GalleryAlbum.objects.filter(is_published=True).prefetch_related("images")
