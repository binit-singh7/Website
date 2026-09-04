from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

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
