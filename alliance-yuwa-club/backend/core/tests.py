from django.test import TestCase

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
