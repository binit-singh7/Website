from django.core.cache import cache
from django.test import TestCase
from rest_framework.test import APITestCase

from .models import ContactMessage


class ContactMessageModelTests(TestCase):
    def test_contact_message_defaults_to_unread(self):
        message = ContactMessage.objects.create(
            name="Example Visitor",
            email="visitor@example.com",
            subject="Membership inquiry",
            message="How can I join?",
        )

        self.assertEqual(message.status, ContactMessage.STATUS_UNREAD)


class ContactMessageApiTests(APITestCase):
    payload = {
        "name": "Example Visitor",
        "email": "visitor@example.com",
        "phone": "9800000000",
        "subject": "Membership inquiry",
        "message": "How can I join?",
    }

    def setUp(self):
        super().setUp()
        cache.clear()

    def tearDown(self):
        cache.clear()
        super().tearDown()

    def test_valid_submission_creates_unread_message(self):
        response = self.client.post("/api/contact/", self.payload, format="json")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            ContactMessage.objects.get().status, ContactMessage.STATUS_UNREAD
        )

    def test_invalid_submission_is_rejected_and_no_public_list_exists(self):
        response = self.client.post(
            "/api/contact/", self.payload | {"email": "invalid"}, format="json"
        )
        list_response = self.client.get("/api/contact/messages/")

        self.assertEqual(response.status_code, 400)
        self.assertIn("email", response.data)
        self.assertEqual(list_response.status_code, 404)

    def test_contact_submission_is_throttled_per_client_ip(self):
        for _ in range(5):
            response = self.client.post("/api/contact/", self.payload, format="json")
            self.assertEqual(response.status_code, 201)

        response = self.client.post("/api/contact/", self.payload, format="json")

        self.assertEqual(response.status_code, 429)
        self.assertIn("detail", response.data)
        self.assertEqual(ContactMessage.objects.count(), 5)
