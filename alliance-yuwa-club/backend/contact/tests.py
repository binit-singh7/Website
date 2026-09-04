from django.test import TestCase

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
