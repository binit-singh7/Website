import re

from rest_framework import serializers

from .models import MembershipApplication


class MembershipApplicationSerializer(serializers.ModelSerializer):
    areas_of_interest = serializers.ListField(
        child=serializers.CharField(max_length=100),
        allow_empty=False,
        max_length=20,
    )

    class Meta:
        model = MembershipApplication
        fields = (
            "full_name",
            "date_of_birth",
            "phone",
            "email",
            "address",
            "ward",
            "occupation",
            "education",
            "areas_of_interest",
            "reason_for_joining",
        )
        extra_kwargs = {
            "full_name": {"max_length": 255},
            "address": {"max_length": 500},
            "occupation": {"max_length": 255},
            "education": {"max_length": 255},
            "reason_for_joining": {"max_length": 2000},
        }

    def validate_phone(self, value):
        if not re.fullmatch(r"\+?[0-9][0-9\s-]{6,28}", value):
            raise serializers.ValidationError("Enter a valid phone number.")
        return value

    def create(self, validated_data):
        validated_data["areas_of_interest"] = ", ".join(
            validated_data["areas_of_interest"]
        )
        return super().create(validated_data)
