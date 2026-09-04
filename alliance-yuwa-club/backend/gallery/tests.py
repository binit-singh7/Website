from datetime import date
from tempfile import TemporaryDirectory

from django.contrib.admin.sites import AdminSite
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory, TestCase, override_settings
from django.utils.datastructures import MultiValueDict
from rest_framework.test import APITestCase

from .admin import GalleryAlbumAdmin, GalleryAlbumAdminForm
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


class GalleryAdminTests(TestCase):
    def setUp(self):
        self.media_directory = TemporaryDirectory()
        self.media_override = override_settings(MEDIA_ROOT=self.media_directory.name)
        self.media_override.enable()

    def tearDown(self):
        self.media_override.disable()
        self.media_directory.cleanup()

    def test_batch_upload_creates_ordered_album_images(self):
        album = GalleryAlbum.objects.create(
            title="Youth Day", slug="youth-day", date=date(2026, 8, 12)
        )
        first_image = SimpleUploadedFile("first.jpg", b"first image")
        second_image = SimpleUploadedFile("second.jpg", b"second image")
        form = GalleryAlbumAdminForm(
            data={
                "title": album.title,
                "slug": album.slug,
                "date": album.date.isoformat(),
            },
            files=MultiValueDict({"batch_images": [first_image, second_image]}),
            instance=album,
        )

        self.assertTrue(form.is_valid())
        form.save(commit=False).save()

        request = RequestFactory().post("/")
        request._files = MultiValueDict({"batch_images": [first_image, second_image]})
        GalleryAlbumAdmin(GalleryAlbum, AdminSite()).save_related(
            request, form, [], change=True
        )

        images = list(GalleryImage.objects.filter(album=album))
        self.assertEqual(len(images), 2)
        self.assertEqual([image.display_order for image in images], [0, 1])


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
