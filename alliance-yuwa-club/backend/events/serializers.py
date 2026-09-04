from rest_framework import serializers

from .models import Event, EventImage


class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ("id", "image", "caption", "display_order")


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "slug",
            "description",
            "start_datetime",
            "end_datetime",
            "location",
            "status",
            "featured",
            "registration_required",
            "registration_url",
            "cover_image",
        )


class EventDetailSerializer(EventSerializer):
    images = EventImageSerializer(many=True, read_only=True)

    class Meta(EventSerializer.Meta):
        fields = EventSerializer.Meta.fields + ("images",)
