import json
import os
from datetime import date
from typing import ClassVar
from unittest.mock import patch
from urllib.error import HTTPError

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.core import mail
from django.core.cache import cache
from django.test import RequestFactory, TestCase, override_settings
from rest_framework.test import APITestCase

from config import settings

from .admin import MembershipApplicationAdmin
from .emails import send_membership_email
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
    payload: ClassVar[dict] = {
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

    @override_settings(
        EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
        DEFAULT_FROM_EMAIL="Alliance Yuwa Club <allianceyuwaclub@gmail.com>",
    )
    def test_valid_submission_sends_personalized_confirmation_email(self):
        response = self.client.post("/api/membership/apply/", self.payload, format="json")

        self.assertEqual(response.status_code, 201)
        application = MembershipApplication.objects.get()
        self.assertEqual(application.status, MembershipApplication.STATUS_PENDING)
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [application.email])
        self.assertIn(application.full_name, mail.outbox[0].body)
        self.assertIn(f"Application Reference: {application.pk}", mail.outbox[0].body)
        self.assertIn("pending review", mail.outbox[0].body)

    @patch(
        "memberships.emails.send_membership_email",
        side_effect=OSError("provider unavailable"),
    )
    def test_email_failure_keeps_saved_application_and_success_response(
        self, send_email
    ):
        response = self.client.post("/api/membership/apply/", self.payload, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertTrue(MembershipApplication.objects.filter(email=self.payload["email"]).exists())
        send_email.assert_called_once()

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


class MembershipApplicationAdminTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.reviewer = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="test-password",
        )
        self.application = MembershipApplication.objects.create(
            full_name="Admin Applicant",
            date_of_birth=date(2002, 4, 10),
            phone="9800000000",
            email="admin-applicant@example.com",
            address="Biratnagar",
            ward="10",
            occupation="Student",
            education="Bachelor",
            areas_of_interest="Environment",
            reason_for_joining="Community service",
        )
        self.admin_instance = MembershipApplicationAdmin(
            MembershipApplication, admin.site
        )
        self.request = self.factory.post("/admin/memberships/membershipapplication/")
        self.request.user = self.reviewer

    @override_settings(
        EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
        DEFAULT_FROM_EMAIL="Alliance Yuwa Club <allianceyuwaclub@gmail.com>",
    )
    @patch.object(MembershipApplicationAdmin, "message_user")
    def test_approval_action_updates_metadata_and_sends_email(self, message_user):
        self.admin_instance.approve_applications(
            self.request,
            MembershipApplication.objects.filter(pk=self.application.pk),
        )

        self.application.refresh_from_db()
        self.assertEqual(
            self.application.status, MembershipApplication.STATUS_APPROVED
        )
        self.assertEqual(self.application.reviewed_by, self.reviewer)
        self.assertIsNotNone(self.application.reviewed_at)
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn(self.application.full_name, mail.outbox[0].body)
        self.assertIn("approved", mail.outbox[0].body)
        message_user.assert_called()

    @override_settings(
        EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
        DEFAULT_FROM_EMAIL="Alliance Yuwa Club <allianceyuwaclub@gmail.com>",
    )
    @patch.object(MembershipApplicationAdmin, "message_user")
    def test_rejection_action_updates_status_and_sends_email(self, message_user):
        self.application.admin_notes = "Internal review note"
        self.application.save(update_fields=("admin_notes",))

        self.admin_instance.reject_applications(
            self.request,
            MembershipApplication.objects.filter(pk=self.application.pk),
        )

        self.application.refresh_from_db()
        self.assertEqual(
            self.application.status, MembershipApplication.STATUS_REJECTED
        )
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn(self.application.full_name, mail.outbox[0].body)
        self.assertIn("unable to approve", mail.outbox[0].body)
        self.assertNotIn(self.application.admin_notes, mail.outbox[0].body)
        message_user.assert_called()

    @override_settings(
        EMAIL_BACKEND="django.core.mail.backends.locmem.EmailBackend",
        DEFAULT_FROM_EMAIL="Alliance Yuwa Club <allianceyuwaclub@gmail.com>",
    )
    @patch.object(MembershipApplicationAdmin, "message_user")
    def test_repeating_same_admin_action_does_not_resend_email(self, message_user):
        queryset = MembershipApplication.objects.filter(pk=self.application.pk)

        self.admin_instance.approve_applications(self.request, queryset)
        self.admin_instance.approve_applications(self.request, queryset)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(
            MembershipApplication.objects.get(pk=self.application.pk).status,
            MembershipApplication.STATUS_APPROVED,
        )
        message_user.assert_called()

    @patch(
        "memberships.admin.send_application_approved_email",
        return_value=False,
    )
    @patch.object(MembershipApplicationAdmin, "message_user")
    def test_review_status_is_kept_when_status_email_fails(
        self, message_user, send_notification
    ):
        self.admin_instance.approve_applications(
            self.request,
            MembershipApplication.objects.filter(pk=self.application.pk),
        )

        self.application.refresh_from_db()
        self.assertEqual(
            self.application.status, MembershipApplication.STATUS_APPROVED
        )
        send_notification.assert_called_once()
        message_user.assert_called()

    def test_email_password_is_loaded_from_environment_setting(self):
        self.assertEqual(
            settings.RESEND_API_KEY,
            os.environ.get("RESEND_API_KEY", ""),
        )


class MembershipEmailProviderTests(TestCase):
    @override_settings(
        EMAIL_PROVIDER="resend",
        RESEND_API_URL="https://api.resend.com/emails",
        RESEND_API_KEY="test-resend-key",
        EMAIL_FROM_EMAIL="no-reply@allianceyuwaclub.org.np",
        EMAIL_FROM_NAME="Alliance Yuwa Club",
        EMAIL_REPLY_TO="allianceyuwaclub@gmail.com",
        DEFAULT_FROM_EMAIL="Alliance Yuwa Club <no-reply@allianceyuwaclub.org.np>",
        EMAIL_API_TIMEOUT=7,
    )
    @patch("memberships.emails.urlopen")
    def test_resend_provider_sends_expected_https_payload(self, urlopen):
        response = urlopen.return_value.__enter__.return_value
        response.status = 200

        sent = send_membership_email(
            to_email="applicant@example.com",
            subject="Subject",
            body="Body",
            notification_type="application_received",
        )

        self.assertTrue(sent)
        request = urlopen.call_args.args[0]
        payload = json.loads(request.data.decode("utf-8"))
        self.assertEqual(payload["from"], "Alliance Yuwa Club <no-reply@allianceyuwaclub.org.np>")
        self.assertEqual(payload["to"], ["applicant@example.com"])
        self.assertEqual(payload["reply_to"], ["allianceyuwaclub@gmail.com"])
        self.assertEqual(payload["text"], "Body")
        self.assertEqual(request.get_header("Authorization"), "Bearer test-resend-key")
        self.assertEqual(urlopen.call_args.kwargs["timeout"], 7)

    @override_settings(
        EMAIL_PROVIDER="resend",
        RESEND_API_KEY="test-resend-key",
        EMAIL_FROM_EMAIL="no-reply@allianceyuwaclub.org.np",
        EMAIL_FROM_NAME="Alliance Yuwa Club",
        EMAIL_REPLY_TO="allianceyuwaclub@gmail.com",
        DEFAULT_FROM_EMAIL="Alliance Yuwa Club <no-reply@allianceyuwaclub.org.np>",
    )
    @patch("memberships.emails.urlopen", side_effect=TimeoutError("timed out"))
    def test_resend_timeout_returns_failure_without_network_retry(self, urlopen):
        self.assertFalse(
            send_membership_email(
                to_email="applicant@example.com",
                subject="Subject",
                body="Body",
                notification_type="application_received",
            )
        )
        urlopen.assert_called_once()

    @override_settings(
        EMAIL_PROVIDER="resend",
        RESEND_API_KEY="test-resend-key",
        EMAIL_FROM_EMAIL="no-reply@allianceyuwaclub.org.np",
        EMAIL_FROM_NAME="Alliance Yuwa Club",
        EMAIL_REPLY_TO="allianceyuwaclub@gmail.com",
        DEFAULT_FROM_EMAIL="Alliance Yuwa Club <no-reply@allianceyuwaclub.org.np>",
    )
    @patch(
        "memberships.emails.urlopen",
        side_effect=HTTPError(
            "https://api.resend.com/emails", 422, "invalid sender", {}, None
        ),
    )
    def test_resend_http_failure_returns_failure_without_exposing_error(
        self, urlopen
    ):
        self.assertFalse(
            send_membership_email(
                to_email="applicant@example.com",
                subject="Subject",
                body="Body",
                notification_type="application_received",
            )
        )
        urlopen.assert_called_once()
