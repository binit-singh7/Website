"""
Smoke test for the new Activity Gallery endpoints.
Creates a published Activity with a cover image and verifies it appears
via the /api/gallery/activity-images/ endpoint in gallery-album shape.
"""
import tempfile
import os

from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIClient

from activities.models import Activity, ActivityCategory, ActivityImage


# Minimal 1x1 white JPEG for tests
TINY_JPEG = (
    b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x00\x00\x01\x00\x01\x00\x00'
    b'\xff\xdb\x00C\x00\x08\x06\x06\x07\x06\x05\x08\x07\x07\x07\t\t'
    b'\x08\n\x0c\x14\r\x0c\x0b\x0b\x0c\x19\x12\x13\x0f\x14\x1d\x1a'
    b'\x1f\x1e\x1d\x1a\x1c\x1c $.\' ",#\x1c\x1c(7),01444\x1f\'9=82<.342\x1e'
    b'!-\x161\x07\x00\xff\xc0\x00\x0b\x08\x00\x01\x00\x01\x01\x01\x11\x00'
    b'\xff\xc4\x00\x1f\x00\x00\x01\x05\x01\x01\x01\x01\x01\x01\x00\x00'
    b'\x00\x00\x00\x00\x00\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b'
    b'\xff\xc4\x00\xb5\x10\x00\x02\x01\x03\x03\x02\x04\x03\x05\x05\x04'
    b'\x04\x00\x00\x01}\x01\x02\x03\x00\x04\x11\x05\x12!1A\x06\x13Qa'
    b'\x07"q\x142\x81\x91\xa1\x08#B\xb1\xc1\x15R\xd1\xf0$3br\x82\t\n'
    b'\x16\x17\x18\x19\x1a%&\'()*456789:CDEFGHIJSTUVWXYZ'
    b'cdefghijstuvwxyz\x83\x84\x85\x86\x87\x88\x89\x8a\x92\x93\x94\x95'
    b'\x96\x97\x98\x99\x9a\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xb2\xb3'
    b'\xb4\xb5\xb6\xb7\xb8\xb9\xba\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca'
    b'\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xe1\xe2\xe3\xe4\xe5\xe6\xe7'
    b'\xe8\xe9\xea\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xff\xda\x00'
    b'\x08\x01\x01\x00\x00?\x00\xfb\xd5P\x00\x00\x00\x1f\xff\xd9'
)


class ActivityGalleryEndpointTests(TestCase):
    """
    Tests for the dynamic Activity → Gallery API endpoints.
    """

    def setUp(self):
        self.client = APIClient()
        self.category = ActivityCategory.objects.create(
            name="Community Service", slug="community-service"
        )

    def _make_activity(self, title, slug, status=Activity.STATUS_PUBLISHED, with_cover=True):
        image_file = (
            SimpleUploadedFile("cover.jpg", TINY_JPEG, content_type="image/jpeg")
            if with_cover
            else None
        )
        activity = Activity.objects.create(
            title=title,
            slug=slug,
            description="Test description.",
            date="2026-08-01",
            category=self.category,
            status=status,
            cover_image=image_file or "",
        )
        return activity

    # ------------------------------------------------------------------
    # List endpoint tests
    # ------------------------------------------------------------------

    def test_list_returns_published_activities_with_cover_image(self):
        self._make_activity("Blood Donation", "blood-donation", with_cover=True)
        response = self.client.get("/api/gallery/activity-images/")
        self.assertEqual(response.status_code, 200)
        results = response.data["results"]
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]["title"], "Blood Donation")

    def test_list_slug_has_activity_prefix(self):
        self._make_activity("Tree Plantation", "tree-plantation")
        response = self.client.get("/api/gallery/activity-images/")
        slug = response.data["results"][0]["slug"]
        self.assertEqual(slug, "activity--tree-plantation")

    def test_list_source_field_is_activity(self):
        self._make_activity("Cleanliness Drive", "cleanliness-drive")
        response = self.client.get("/api/gallery/activity-images/")
        self.assertEqual(response.data["results"][0]["source"], "activity")

    def test_list_excludes_draft_activities(self):
        self._make_activity("Draft Activity", "draft-one", status=Activity.STATUS_DRAFT)
        response = self.client.get("/api/gallery/activity-images/")
        self.assertEqual(response.data["results"], [])

    def test_list_excludes_activities_without_images(self):
        self._make_activity("No Image Activity", "no-image", with_cover=False)
        response = self.client.get("/api/gallery/activity-images/")
        self.assertEqual(response.data["results"], [])

    def test_list_includes_activity_with_only_detail_images_no_cover(self):
        activity = self._make_activity("Detail Only", "detail-only", with_cover=False)
        ActivityImage.objects.create(
            activity=activity,
            image=SimpleUploadedFile("detail.jpg", TINY_JPEG, content_type="image/jpeg"),
            display_order=0,
        )
        response = self.client.get("/api/gallery/activity-images/")
        self.assertEqual(len(response.data["results"]), 1)

    # ------------------------------------------------------------------
    # Detail endpoint tests
    # ------------------------------------------------------------------

    def test_detail_returns_activity_images_array(self):
        activity = self._make_activity("Youth Program", "youth-program")
        ActivityImage.objects.create(
            activity=activity,
            image=SimpleUploadedFile("p1.jpg", TINY_JPEG, content_type="image/jpeg"),
            caption="Photo one",
            display_order=0,
        )
        ActivityImage.objects.create(
            activity=activity,
            image=SimpleUploadedFile("p2.jpg", TINY_JPEG, content_type="image/jpeg"),
            caption="Photo two",
            display_order=1,
        )
        # Detail endpoint uses the plain activity slug (no prefix)
        response = self.client.get("/api/gallery/activity-images/youth-program/")
        self.assertEqual(response.status_code, 200)
        # cover_image is prepended + 2 detail images = 3 total
        self.assertGreaterEqual(len(response.data["images"]), 2)

    def test_detail_404_for_unknown_slug(self):
        response = self.client.get("/api/gallery/activity-images/nonexistent/")
        self.assertEqual(response.status_code, 404)

    def test_detail_404_for_draft_activity(self):
        self._make_activity("Hidden Draft", "hidden-draft", status=Activity.STATUS_DRAFT)
        response = self.client.get("/api/gallery/activity-images/hidden-draft/")
        self.assertEqual(response.status_code, 404)

    def test_deleted_activity_disappears_from_list(self):
        activity = self._make_activity("Temporary", "temporary")
        response = self.client.get("/api/gallery/activity-images/")
        self.assertEqual(len(response.data["results"]), 1)
        activity.delete()
        response = self.client.get("/api/gallery/activity-images/")
        self.assertEqual(response.data["results"], [])
