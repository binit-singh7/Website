from datetime import date

from django.test import TestCase
from rest_framework.test import APITestCase

from .models import GalleryAlbum, GalleryImage


class GalleryModelTests(TestCase):
    def test_album_defaults_and_image_cascade(self):
        album = GalleryAlbum.objects.create(
            title="Youth Day", slug="youth-day", date=date(2026, 8, 12)
        )
        image = GalleryImage.objects.create(album=album, image="gallery.jpg")

        self.assertFalse(album.is_published)
        album.delete()
        self.assertFalse(GalleryImage.objects.filter(pk=image.pk).exists())


class GalleryApiTests(APITestCase):
    def setUp(self):
        self.album = GalleryAlbum.objects.create(
            title="Published Album",
            slug="published-album",
            date=date(2026, 8, 12),
            is_published=True,
        )
        GalleryAlbum.objects.create(
            title="Draft Album",
            slug="draft-album",
            date=date(2026, 8, 11),
        )

    def test_list_and_detail_expose_only_published_albums(self):
        GalleryImage.objects.create(album=self.album, image="gallery.jpg")

        list_response = self.client.get("/api/gallery/albums/")
        detail_response = self.client.get("/api/gallery/albums/published-album/")
        draft_response = self.client.get("/api/gallery/albums/draft-album/")

        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(list_response.data["count"], 1)
        self.assertEqual(detail_response.status_code, 200)
        self.assertEqual(len(detail_response.data["images"]), 1)
        self.assertEqual(draft_response.status_code, 404)
