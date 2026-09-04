import re

from rest_framework import serializers

from .models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ("name", "email", "phone", "subject", "message")
        extra_kwargs = {
            "name": {"max_length": 255},
            "subject": {"max_length": 255},
            "message": {"max_length": 2000},
        }

    def validate_phone(self, value):
        if value and not re.fullmatch(r"\+?[0-9][0-9\s-]{6,28}", value):
            raise serializers.ValidationError("Enter a valid phone number.")
        return value
