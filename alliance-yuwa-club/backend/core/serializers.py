from rest_framework import serializers

from .models import Announcement, Organization


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = (
            "name",
            "short_name",
            "description",
            "motto",
            "vision",
            "mission",
            "address",
            "phone",
            "email",
            "facebook_url",
            "instagram_url",
            "youtube_url",
            "logo",
        )


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ("id", "title", "content", "priority", "start_date", "end_date")
