from datetime import date

from django.db import IntegrityError, transaction
from django.db.models.deletion import ProtectedError
from django.test import TestCase
from rest_framework.test import APITestCase

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


class ActivityApiTests(APITestCase):
    def setUp(self):
        self.category = ActivityCategory.objects.create(
            name="Environment", slug="environment"
        )
        self.published = Activity.objects.create(
            title="Published Activity",
            slug="published-activity",
            description="Visible",
            date=date(2026, 8, 12),
            category=self.category,
            featured=True,
            status=Activity.STATUS_PUBLISHED,
        )
        Activity.objects.create(
            title="Draft Activity",
            slug="draft-activity",
            description="Hidden",
            date=date(2025, 8, 12),
            category=self.category,
        )

    def test_list_filters_published_category_year_featured_and_paginates(self):
        response = self.client.get(
            "/api/activities/?category=environment&year=2026&featured=true&page_size=1"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["slug"], self.published.slug)

    def test_detail_includes_images_and_hides_drafts(self):
        ActivityImage.objects.create(activity=self.published, image="activity.jpg")

        response = self.client.get("/api/activities/published-activity/")
        draft_response = self.client.get("/api/activities/draft-activity/")
        missing_response = self.client.get("/api/activities/missing/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["images"]), 1)
        self.assertEqual(draft_response.status_code, 404)
        self.assertEqual(missing_response.status_code, 404)
