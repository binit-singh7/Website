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


# ---------------------------------------------------------------------------
# Virtual serializers — map Activity data into gallery-shaped responses.
# No database records are created; these are read-only views of Activity data.
# ---------------------------------------------------------------------------

class ActivityImageAsGalleryImageSerializer(serializers.Serializer):
    """Serialize an ActivityImage as if it were a GalleryImage."""
    id = serializers.IntegerField()
    image = serializers.ImageField()
    caption = serializers.CharField()
    display_order = serializers.IntegerField()


class ActivityAsAlbumSerializer(serializers.Serializer):
    """
    Serialize a published Activity as if it were a GalleryAlbum.

    The slug is prefixed with 'activity--' so the frontend can distinguish
    activity-sourced items from manually created gallery albums, and route
    detail requests to the correct API endpoint.
    """
    id = serializers.IntegerField()
    title = serializers.CharField()
    slug = serializers.SerializerMethodField()
    description = serializers.CharField()
    date = serializers.DateField()
    cover_image = serializers.ImageField(allow_null=True)
    # Extra field the frontend uses to drive the correct detail fetch
    source = serializers.SerializerMethodField()

    def get_slug(self, obj):
        return f"activity--{obj.slug}"

    def get_source(self, obj):
        return "activity"


class ActivityAsAlbumDetailSerializer(ActivityAsAlbumSerializer):
    """
    Full detail shape for a single Activity surfaced through the gallery.

    Builds an images[] array from ActivityImage records. If the activity
    also has a cover_image and it is not already in the images set, it is
    prepended as the first entry (id=0, display_order=-1) so the gallery
    lightbox always has at least one image to show.
    """
    images = serializers.SerializerMethodField()

    def get_images(self, obj):
        from activities.models import ActivityImage

        detail_images = list(
            ActivityImage.objects.filter(activity=obj).order_by("display_order", "id")
        )

        result = []
        cover_name = obj.cover_image.name if obj.cover_image else None

        # Prepend cover_image if it is not already represented in ActivityImage
        if cover_name and not any(img.image.name == cover_name for img in detail_images):
            result.append({
                "id": 0,
                "image": obj.cover_image,
                "caption": obj.title,
                "display_order": -1,
            })

        for img in detail_images:
            result.append({
                "id": img.id,
                "image": img.image,
                "caption": img.caption,
                "display_order": img.display_order,
            })

        # Serialize the assembled list using the request context for absolute URLs
        request = self.context.get("request")
        serialized = []
        for entry in result:
            image_field = serializers.ImageField()
            image_field.bind("image", self)
            image_field._context = {"request": request}
            serialized.append({
                "id": entry["id"],
                "image": request.build_absolute_uri(entry["image"].url) if entry["image"] else None,
                "caption": entry["caption"],
                "display_order": entry["display_order"],
            })
        return serialized
