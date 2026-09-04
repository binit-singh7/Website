from datetime import date

from django.db import IntegrityError, transaction
from django.db.models.deletion import ProtectedError
from django.test import TestCase

from .models import Activity, ActivityCategory, ActivityImage


class ActivityModelTests(TestCase):
    def setUp(self):
        self.category = ActivityCategory.objects.create(
            name="Environment", slug="environment"
        )

    def test_activity_defaults_and_category_protection(self):
        activity = Activity.objects.create(
            title="Border Cleanup",
            slug="border-cleanup",
            description="Cleanup drive",
            date=date(2026, 8, 12),
            category=self.category,
        )

        self.assertEqual(activity.status, Activity.STATUS_DRAFT)
        with self.assertRaises(ProtectedError):
            self.category.delete()

    def test_category_slug_is_unique_and_images_are_deleted_with_activity(self):
        with self.assertRaises(IntegrityError), transaction.atomic():
            ActivityCategory.objects.create(name="Environment Two", slug="environment")

        activity = Activity.objects.create(
            title="Cleanup Two",
            slug="cleanup-two",
            description="Cleanup drive",
            date=date(2026, 8, 13),
            category=self.category,
        )
        image = ActivityImage.objects.create(activity=activity, image="activity.jpg")

        activity.delete()

        self.assertFalse(ActivityImage.objects.filter(pk=image.pk).exists())
