"""
Django-generated sitemap for the public Alliance Yuwa Club website.

The sitemap is generated from the database so it always reflects the currently
published public records (activities, events, news, gallery albums) plus the
fixed public pages. It deliberately excludes admin, API endpoints, draft/
unpublished/archived records, and non-indexable utility routes.

Canonical URLs use the public frontend origin (allianceyuwaclub.org.np) so the
sitemap is correct regardless of which host serves it. The domain is passed
explicitly to the sitemap generators, so ``django.contrib.sitemaps`` works
without ``django.contrib.sites``.
"""

from types import SimpleNamespace

from django.contrib.sitemaps import Sitemap
from django.contrib.sitemaps.views import x_robots_tag
from django.template.response import TemplateResponse
from django.views.decorators.http import require_GET

from activities.models import Activity
from events.models import Event
from gallery.models import GalleryAlbum
from news.models import NewsArticle


def frontend_base_url():
    """Public frontend origin used to build canonical sitemap URLs."""
    from django.conf import settings

    return getattr(
        settings,
        "FRONTEND_BASE_URL",
        "https://allianceyuwaclub.org.np",
    ).rstrip("/")


def _frontend_site():
    """A lightweight site object with a ``domain`` attribute for the sitemap
    generators, mirroring what ``django.contrib.sites`` would provide."""
    base = frontend_base_url()
    if "://" in base:
        domain = base.split("://", 1)[1]
    else:
        domain = base
    return SimpleNamespace(domain=domain, name="Alliance Yuwa Club")


class StaticViewSitemap(Sitemap):
    """Fixed public pages that exist as client-side routes."""

    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return [
            "/",
            "/about/",
            "/activities/",
            "/events/",
            "/news/",
            "/team/",
            "/gallery/",
            "/membership/",
            "/contact/",
        ]

    def location(self, item):
        return item


class ActivitySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Activity.objects.filter(status=Activity.STATUS_PUBLISHED)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return f"/activities/{obj.slug}/"


class EventSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        # Public events exclude drafts; cancelled/completed remain public.
        return Event.objects.exclude(status=Event.STATUS_DRAFT)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return f"/events/{obj.slug}/"


class NewsSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return NewsArticle.objects.filter(status=NewsArticle.STATUS_PUBLISHED)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return f"/news/{obj.slug}/"


class GallerySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return GalleryAlbum.objects.filter(is_published=True)

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return f"/gallery/{obj.slug}/"


sitemaps = {
    "activities": ActivitySitemap,
    "events": EventSitemap,
    "news": NewsSitemap,
    "gallery": GallerySitemap,
    "static": StaticViewSitemap,
}


@x_robots_tag
@require_GET
def sitemap_view(request):
    """Render a single ``sitemap.xml`` combining every public URL.

    The frontend origin is supplied explicitly so the published URLs point at
    the public site regardless of the host that serves this view.
    """
    site = _frontend_site()
    protocol = "https"
    urlset = []
    for sitemap_cls in sitemaps.values():
        urlset.extend(
            sitemap_cls().get_urls(site=site, protocol=protocol)
        )
    return TemplateResponse(
        request,
        "sitemap.xml",
        {"urlset": urlset},
        content_type="application/xml",
    )
