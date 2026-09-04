from django.test import TestCase
from rest_framework.test import APITestCase

from .models import Announcement, Organization


class CoreModelTests(TestCase):
    def test_organization_and_announcement_defaults(self):
        organization = Organization.objects.create(name="Alliance Yuwa Club")
        announcement = Announcement.objects.create(
            title="Notice", content="Club notice"
        )

        self.assertEqual(str(organization), "Alliance Yuwa Club")
        self.assertTrue(announcement.is_active)
        self.assertEqual(announcement.priority, Announcement.PRIORITY_NORMAL)


class HealthCheckTests(TestCase):
    def test_health_check_returns_ok(self):
        response = self.client.get("/api/health/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})


class CoreApiTests(APITestCase):
    def test_organization_returns_public_fields_only(self):
        Organization.objects.create(name="Alliance Yuwa Club", phone="9800000000")

        response = self.client.get("/api/organization/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Alliance Yuwa Club")
        self.assertNotIn("created_at", response.data)
        self.assertNotIn("updated_at", response.data)

    def test_active_current_announcements_are_returned(self):
        Announcement.objects.create(title="Active", content="Visible")
        Announcement.objects.create(title="Inactive", content="Hidden", is_active=False)

        response = self.client.get("/api/announcements/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual([item["title"] for item in response.data], ["Active"])
