from datetime import date, datetime
from urllib.parse import urlparse

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.files.storage import default_storage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import SimpleTestCase, TestCase
from django.utils import timezone
from django.utils.module_loading import import_string
from rest_framework.test import APITestCase
from storages.backends.s3boto3 import S3Boto3Storage

from activities.models import Activity, ActivityCategory, ActivityImage
from config.settings import get_list_setting, get_media_storage_configuration
from events.models import Event, EventImage
from gallery.models import GalleryAlbum, GalleryImage
from news.models import NewsArticle
from team.models import TeamMember

from .models import Announcement, Organization
from .validators import (
    MAX_IMAGE_UPLOAD_SIZE,
    image_upload_validators,
    validate_image_extension,
    validate_image_file_size,
)


class MediaStorageConfigurationTests(SimpleTestCase):
    def test_local_storage_is_used_when_supabase_storage_is_disabled(self):
        configuration = get_media_storage_configuration(
            {"USE_SUPABASE_STORAGE": "False"}
        )

        self.assertEqual(configuration["media_url"], "/media/")
        self.assertEqual(
            configuration["storages"]["default"]["BACKEND"],
            "django.core.files.storage.FileSystemStorage",
        )

    def test_supabase_storage_uses_s3_backend_and_public_media_url(self):
        configuration = get_media_storage_configuration(
            {
                "USE_SUPABASE_STORAGE": "True",
                "SUPABASE_STORAGE_BUCKET": "club-media",
                "SUPABASE_S3_ACCESS_KEY_ID": "test-access-key",
                "SUPABASE_S3_SECRET_ACCESS_KEY": "test-secret-key",
                "SUPABASE_S3_ENDPOINT_URL": "https://project.supabase.co/storage/v1/s3",
            }
        )
        default_storage_settings = configuration["storages"]["default"]

        self.assertEqual(
            default_storage_settings["BACKEND"],
            "storages.backends.s3boto3.S3Boto3Storage",
        )
        storage_class = import_string(default_storage_settings["BACKEND"])
        self.assertIs(storage_class, S3Boto3Storage)
        self.assertEqual(
            configuration["media_url"],
            "https://project.supabase.co/storage/v1/object/public/club-media/",
        )
        self.assertEqual(default_storage_settings["OPTIONS"]["region_name"], "us-east-1")
        self.assertFalse(default_storage_settings["OPTIONS"]["querystring_auth"])


class ProductionEnvironmentParsingTests(SimpleTestCase):
    """Regression tests for comma-separated production environment parsing.

    These cover the production-readiness audit finding that ALLOWED_HOSTS,
    CORS_ALLOWED_ORIGINS, and CSRF_TRUSTED_ORIGINS must safely split
    comma-separated environment strings (for example
    ``https://allianceyuwaclub.org.np,https://*.vercel.app``) into lists,
    trimming whitespace and dropping blank entries.
    """

    def test_allowed_hosts_splits_and_strips_comma_separated_values(self):
        hosts = get_list_setting(
            "ALLOWED_HOSTS",
            environment={
                "ALLOWED_HOSTS": " allianceyuwaclub.org.np , .onrender.com ,,"
            },
        )

        self.assertEqual(hosts, ["allianceyuwaclub.org.np", ".onrender.com"])

    def test_cors_origins_parse_https_and_wildcard_entries(self):
        origins = get_list_setting(
            "CORS_ALLOWED_ORIGINS",
            environment={
                "CORS_ALLOWED_ORIGINS": (
                    "https://allianceyuwaclub.org.np,"
                    "https://*.vercel.app,"
                )
            },
        )

        self.assertEqual(
            origins,
            ["https://allianceyuwaclub.org.np", "https://*.vercel.app"],
        )

    def test_csrf_trusted_origins_parse_comma_separated_values(self):
        origins = get_list_setting(
            "CSRF_TRUSTED_ORIGINS",
            environment={
                "CSRF_TRUSTED_ORIGINS": (
                    "https://allianceyuwaclub.org.np, https://*.vercel.app"
                )
            },
        )

        self.assertEqual(
            origins,
            ["https://allianceyuwaclub.org.np", "https://*.vercel.app"],
        )

    def test_missing_value_falls_back_to_default(self):
        self.assertEqual(
            get_list_setting(
                "ALLOWED_HOSTS", "localhost,127.0.0.1", environment={}
            ),
            ["localhost", "127.0.0.1"],
        )

    def test_empty_string_yields_empty_list(self):
        self.assertEqual(
            get_list_setting(
                "CSRF_TRUSTED_ORIGINS",
                environment={"CSRF_TRUSTED_ORIGINS": ""},
            ),
            [],
        )

    def test_settings_expose_parsed_lists(self):
        for setting_name in (
            "ALLOWED_HOSTS",
            "CORS_ALLOWED_ORIGINS",
            "CSRF_TRUSTED_ORIGINS",
        ):
            with self.subTest(setting_name=setting_name):
                self.assertIsInstance(getattr(settings, setting_name), list)


class ImageUploadValidatorTests(SimpleTestCase):
    def test_valid_image_extensions_under_size_limit_are_accepted(self):
        for extension in ("jpg", "png", "webp"):
            with self.subTest(extension=extension):
                uploaded_file = SimpleUploadedFile(f"image.{extension}", b"image")
                for validator in image_upload_validators:
                    validator(uploaded_file)

    def test_oversized_image_is_rejected(self):
        uploaded_file = SimpleUploadedFile(
            "oversized.jpg", b"x" * (MAX_IMAGE_UPLOAD_SIZE + 1)
        )

        with self.assertRaisesMessage(ValidationError, "5 MB or smaller"):
            validate_image_file_size(uploaded_file)

    def test_disallowed_image_extension_is_rejected(self):
        uploaded_file = SimpleUploadedFile("unsupported.gif", b"image")

        with self.assertRaisesMessage(ValidationError, ".jpg, .jpeg, .png, or .webp"):
            validate_image_extension(uploaded_file)

    def test_all_model_image_fields_use_shared_validators(self):
        image_fields = (
            Activity._meta.get_field("cover_image"),
            ActivityImage._meta.get_field("image"),
            Event._meta.get_field("cover_image"),
            EventImage._meta.get_field("image"),
            NewsArticle._meta.get_field("featured_image"),
            TeamMember._meta.get_field("photo"),
            Organization._meta.get_field("logo"),
            GalleryAlbum._meta.get_field("cover_image"),
            GalleryImage._meta.get_field("image"),
        )

        for image_field in image_fields:
            with self.subTest(field=image_field.name):
                validators_are_attached = all(
                    validator in image_field.validators
                    for validator in image_upload_validators
                )
                self.assertTrue(validators_are_attached)


class CoreModelTests(TestCase):
    def test_organization_and_announcement_defaults(self):
        organization = Organization.objects.create(name="Alliance Yuwa Club")
        announcement = Announcement.objects.create(
            title="Notice", content="Club notice"
        )

        self.assertEqual(str(organization), "Alliance Yuwa Club")
        self.assertTrue(announcement.is_active)
        self.assertEqual(announcement.priority, Announcement.PRIORITY_NORMAL)


class HealthCheckTests(TestCase):
    def test_health_check_returns_ok(self):
        response = self.client.get("/api/health/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})


class CoreApiTests(APITestCase):
    def test_organization_returns_public_fields_only(self):
        Organization.objects.create(name="Alliance Yuwa Club", phone="9800000000")

        response = self.client.get("/api/organization/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["name"], "Alliance Yuwa Club")
        self.assertNotIn("created_at", response.data)
        self.assertNotIn("updated_at", response.data)

    def test_active_current_announcements_are_returned(self):
        Announcement.objects.create(title="Active", content="Visible")
        Announcement.objects.create(title="Inactive", content="Hidden", is_active=False)

        response = self.client.get("/api/announcements/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual([item["title"] for item in response.data], ["Active"])


class PublicMediaSerializationTests(APITestCase):
    """Ensure every public ImageField has a usable URL without reading a file."""

    def setUp(self):
        category = ActivityCategory.objects.create(
            name="Environment", slug="environment"
        )
        activity = Activity.objects.create(
            title="Image Activity",
            slug="image-activity",
            description="Published activity with media.",
            date=date(2026, 8, 12),
            category=category,
            status=Activity.STATUS_PUBLISHED,
            cover_image="activities/activity-cover.jpg",
        )
        ActivityImage.objects.create(
            activity=activity, image="activities/images/activity-image.jpg"
        )

        event = Event.objects.create(
            title="Image Event",
            slug="image-event",
            description="Published event with media.",
            start_datetime=datetime(
                2026, 9, 15, 10, 0, tzinfo=timezone.get_current_timezone()
            ),
            status=Event.STATUS_UPCOMING,
            cover_image="events/event-cover.jpg",
        )
        EventImage.objects.create(event=event, image="events/images/event-image.jpg")

        NewsArticle.objects.create(
            title="Image News",
            slug="image-news",
            content="Published news with media.",
            status=NewsArticle.STATUS_PUBLISHED,
            published_at=timezone.now(),
            featured_image="news/news-image.jpg",
        )
        TeamMember.objects.create(
            name="Image Member",
            position="Member",
            photo="team/member-photo.jpg",
        )
        album = GalleryAlbum.objects.create(
            title="Image Album",
            slug="image-album",
            date=date(2026, 8, 12),
            cover_image="gallery/album-cover.jpg",
            is_published=True,
        )
        GalleryImage.objects.create(
            album=album, image="gallery/images/gallery-image.jpg"
        )
        Organization.objects.create(
            name="Alliance Yuwa Club", logo="organization/club-logo.jpg"
        )

    def assert_media_url(self, value, expected_path):
        self.assertIsInstance(value, str)
        self.assertEqual(urlparse(value).path, f"/media/{expected_path}")
        self.assertNotIn(str(settings.MEDIA_ROOT), value)

    def test_default_storage_uses_media_urls(self):
        self.assertEqual(
            settings.STORAGES["default"]["BACKEND"],
            "django.core.files.storage.FileSystemStorage",
        )
        self.assert_media_url(
            default_storage.url("organization/club-logo.jpg"),
            "organization/club-logo.jpg",
        )

    def test_public_api_serializes_all_image_fields(self):
        activity = self.client.get("/api/activities/image-activity/")
        event = self.client.get("/api/events/image-event/")
        news = self.client.get("/api/news/image-news/")
        team = self.client.get("/api/team/")
        gallery = self.client.get("/api/gallery/albums/image-album/")
        organization = self.client.get("/api/organization/")

        for response in (activity, event, news, team, gallery, organization):
            self.assertEqual(response.status_code, 200)

        self.assert_media_url(activity.data["cover_image"], "activities/activity-cover.jpg")
        self.assert_media_url(
            activity.data["images"][0]["image"], "activities/images/activity-image.jpg"
        )
        self.assert_media_url(event.data["cover_image"], "events/event-cover.jpg")
        self.assert_media_url(
            event.data["images"][0]["image"], "events/images/event-image.jpg"
        )
        self.assert_media_url(news.data["featured_image"], "news/news-image.jpg")
        self.assert_media_url(team.data[0]["photo"], "team/member-photo.jpg")
        self.assert_media_url(gallery.data["cover_image"], "gallery/album-cover.jpg")
        self.assert_media_url(
            gallery.data["images"][0]["image"], "gallery/images/gallery-image.jpg"
        )
        self.assert_media_url(organization.data["logo"], "organization/club-logo.jpg")


class SitemapTests(TestCase):
    """The Django-generated sitemap lists only public, published URLs.

    Draft/unpublished records and admin/API routes must never appear, and every
    URL must use the public frontend origin.
    """

    def setUp(self):
        category = ActivityCategory.objects.create(
            name="Environment", slug="environment"
        )
        Activity.objects.create(
            title="Published Activity",
            slug="published-activity",
            description="Published activity description.",
            date=date(2026, 8, 12),
            category=category,
            status=Activity.STATUS_PUBLISHED,
        )
        Activity.objects.create(
            title="Draft Activity",
            slug="draft-activity",
            description="Draft activity description.",
            date=date(2026, 8, 12),
            category=category,
            status=Activity.STATUS_DRAFT,
        )
        Event.objects.create(
            title="Completed Event",
            slug="completed-event",
            description="Completed event description.",
            start_datetime=datetime(
                2026, 8, 12, 10, 0, tzinfo=timezone.get_current_timezone()
            ),
            status=Event.STATUS_COMPLETED,
        )
        Event.objects.create(
            title="Draft Event",
            slug="draft-event",
            description="Draft event description.",
            start_datetime=datetime(
                2026, 8, 12, 10, 0, tzinfo=timezone.get_current_timezone()
            ),
            status=Event.STATUS_DRAFT,
        )
        NewsArticle.objects.create(
            title="Published News",
            slug="published-news",
            content="Published news content.",
            status=NewsArticle.STATUS_PUBLISHED,
            published_at=timezone.now(),
        )
        NewsArticle.objects.create(
            title="Draft News",
            slug="draft-news",
            content="Draft news content.",
            status=NewsArticle.STATUS_DRAFT,
        )
        GalleryAlbum.objects.create(
            title="Published Album",
            slug="published-album",
            date=date(2026, 8, 12),
            is_published=True,
        )
        GalleryAlbum.objects.create(
            title="Unpublished Album",
            slug="unpublished-album",
            date=date(2026, 8, 12),
            is_published=False,
        )

    def _content(self):
        response = self.client.get("/sitemap.xml")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response["Content-Type"], "application/xml"
        )
        return response.content.decode("utf-8")

    def test_sitemap_uses_public_frontend_origin(self):
        content = self._content()
        self.assertIn("https://allianceyuwaclub.org.np", content)

    def test_sitemap_includes_published_records_and_static_pages(self):
        content = self._content()
        for url in (
            "https://allianceyuwaclub.org.np/",
            "https://allianceyuwaclub.org.np/about/",
            "https://allianceyuwaclub.org.np/activities/published-activity/",
            "https://allianceyuwaclub.org.np/events/completed-event/",
            "https://allianceyuwaclub.org.np/news/published-news/",
            "https://allianceyuwaclub.org.np/gallery/published-album/",
            "https://allianceyuwaclub.org.np/team/",
            "https://allianceyuwaclub.org.np/contact/",
        ):
            with self.subTest(url=url):
                self.assertIn(url, content)

    def test_sitemap_excludes_unpublished_and_private_routes(self):
        content = self._content()
        for url in (
            "/activities/draft-activity/",
            "/events/draft-event/",
            "/news/draft-news/",
            "/gallery/unpublished-album/",
            "/admin",
            "/api",
        ):
            with self.subTest(url=url):
                self.assertNotIn(url, content)
