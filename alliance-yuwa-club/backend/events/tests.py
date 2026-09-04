from datetime import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Event, EventImage


class EventModelTests(TestCase):
    def test_event_defaults_and_image_cascade(self):
        event = Event.objects.create(
            title="Youth Convention",
            slug="youth-convention",
            description="Convention",
            start_datetime=datetime(
                2026, 9, 15, 10, 0, tzinfo=timezone.get_current_timezone()
            ),
        )
        image = EventImage.objects.create(event=event, image="event.jpg")

        self.assertEqual(event.status, Event.STATUS_DRAFT)
        event.delete()
        self.assertFalse(EventImage.objects.filter(pk=image.pk).exists())
