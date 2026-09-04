from datetime import date

from django.test import TestCase

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
