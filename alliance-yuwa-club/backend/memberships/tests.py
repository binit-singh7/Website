from datetime import date

from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.test import TestCase
from rest_framework.test import APITestCase

from .models import MembershipApplication


class MembershipApplicationModelTests(TestCase):
    def test_default_status_and_reviewer_deletion(self):
        reviewer = get_user_model().objects.create_user(
            username="reviewer", password="test-password"
        )
        application = MembershipApplication.objects.create(
            full_name="Example Applicant",
            date_of_birth=date(2002, 4, 10),
            phone="9800000000",
            email="applicant@example.com",
            address="Biratnagar",
            ward="10",
            occupation="Student",
            education="Bachelor",
            areas_of_interest="Environment",
            reason_for_joining="Community service",
            reviewed_by=reviewer,
        )

        reviewer.delete()
        application.refresh_from_db()

        self.assertEqual(application.status, MembershipApplication.STATUS_PENDING)
        self.assertIsNone(application.reviewed_by)


class MembershipApplicationApiTests(APITestCase):
    payload = {
        "full_name": "Example Applicant",
        "date_of_birth": "2002-04-10",
        "phone": "9800000000",
        "email": "applicant@example.com",
        "address": "Biratnagar",
        "ward": "10",
        "occupation": "Student",
        "education": "Bachelor",
        "areas_of_interest": ["Environment", "Social Service"],
        "reason_for_joining": "Community service",
    }

    def setUp(self):
        super().setUp()
        cache.clear()

    def tearDown(self):
        cache.clear()
        super().tearDown()

    def test_valid_submission_creates_pending_application_without_admin_control(self):
        payload = self.payload | {"status": "approved", "admin_notes": "Ignore"}

        response = self.client.post("/api/membership/apply/", payload, format="json")

        self.assertEqual(response.status_code, 201)
        application = MembershipApplication.objects.get()
        self.assertEqual(application.status, MembershipApplication.STATUS_PENDING)
        self.assertEqual(application.areas_of_interest, "Environment, Social Service")
        self.assertEqual(application.admin_notes, "")

    def test_invalid_submission_returns_field_errors(self):
        response = self.client.post(
            "/api/membership/apply/", self.payload | {"phone": "invalid"}, format="json"
        )

        self.assertEqual(response.status_code, 400)
        self.assertIn("phone", response.data)

    def test_membership_application_is_throttled_per_client_ip(self):
        for _ in range(3):
            response = self.client.post(
                "/api/membership/apply/", self.payload, format="json"
            )
            self.assertEqual(response.status_code, 201)

        response = self.client.post(
            "/api/membership/apply/", self.payload, format="json"
        )

        self.assertEqual(response.status_code, 429)
        self.assertIn("detail", response.data)
        self.assertEqual(MembershipApplication.objects.count(), 3)
