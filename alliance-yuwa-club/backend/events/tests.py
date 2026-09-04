from datetime import datetime

from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APITestCase

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


class EventApiTests(APITestCase):
    def setUp(self):
        self.upcoming = Event.objects.create(
            title="Upcoming Event",
            slug="upcoming-event",
            description="Visible",
            start_datetime=datetime(
                2026, 9, 15, 10, 0, tzinfo=timezone.get_current_timezone()
            ),
            status=Event.STATUS_UPCOMING,
            featured=True,
        )
        Event.objects.create(
            title="Completed Event",
            slug="completed-event",
            description="Visible",
            start_datetime=datetime(
                2025, 9, 15, 10, 0, tzinfo=timezone.get_current_timezone()
            ),
            status=Event.STATUS_COMPLETED,
        )
        Event.objects.create(
            title="Draft Event",
            slug="draft-event",
            description="Hidden",
            start_datetime=datetime(
                2026, 10, 15, 10, 0, tzinfo=timezone.get_current_timezone()
            ),
        )

    def test_list_filters_status_year_featured_and_paginates(self):
        response = self.client.get(
            "/api/events/?status=upcoming&year=2026&featured=true&page_size=1"
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["slug"], self.upcoming.slug)

    def test_detail_includes_images_and_hides_drafts(self):
        EventImage.objects.create(event=self.upcoming, image="event.jpg")

        response = self.client.get("/api/events/upcoming-event/")
        draft_response = self.client.get("/api/events/draft-event/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["images"]), 1)
        self.assertEqual(draft_response.status_code, 404)
