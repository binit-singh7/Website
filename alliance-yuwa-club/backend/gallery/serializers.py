from rest_framework import serializers

from .models import GalleryAlbum, GalleryImage


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ("id", "image", "caption", "display_order")


class GalleryAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryAlbum
        fields = ("id", "title", "slug", "description", "date", "cover_image")


class GalleryAlbumDetailSerializer(GalleryAlbumSerializer):
    images = GalleryImageSerializer(many=True, read_only=True)

    class Meta(GalleryAlbumSerializer.Meta):
        fields = GalleryAlbumSerializer.Meta.fields + ("images",)
