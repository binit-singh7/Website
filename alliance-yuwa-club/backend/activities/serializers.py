from rest_framework import serializers

from .models import Activity, ActivityCategory, ActivityImage


class ActivityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityCategory
        fields = ("id", "name", "slug")


class ActivityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityImage
        fields = ("id", "image", "caption", "display_order")


class ActivityListSerializer(serializers.ModelSerializer):
    category = ActivityCategorySerializer(read_only=True)

    class Meta:
        model = Activity
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "date",
            "location",
            "category",
            "featured",
            "cover_image",
        )


class ActivityDetailSerializer(ActivityListSerializer):
    images = ActivityImageSerializer(many=True, read_only=True)

    class Meta(ActivityListSerializer.Meta):
        fields = ActivityListSerializer.Meta.fields + ("images",)
