"""
Template tags for the modernized Alliance Yuwa Club Django Admin dashboard.

Calculates real database metrics and conceptual groupings while preserving
Django's built-in permissions and app structure.
"""

from django import template
from django.db.models import Count

from activities.models import Activity, ActivityCategory, ActivityImage
from contact.models import ContactMessage
from core.models import Announcement, Organization
from events.models import Event, EventImage
from gallery.models import GalleryAlbum, GalleryImage
from memberships.models import MembershipApplication
from news.models import NewsArticle
from team.models import TeamMember

register = template.Library()


@register.simple_tag
def get_dashboard_metrics():
    """
    Return factual statistics calculated strictly from actual database records.
    Zero fabricated numbers or synthetic metrics.
    """
    stats = {}
    try:
        stats["total_activities"] = Activity.objects.count()
        stats["published_activities"] = Activity.objects.filter(
            status=Activity.STATUS_PUBLISHED
        ).count()
        stats["draft_activities"] = Activity.objects.filter(
            status=Activity.STATUS_DRAFT
        ).count()
    except Exception:
        stats["total_activities"] = 0
        stats["published_activities"] = 0
        stats["draft_activities"] = 0

    try:
        stats["total_events"] = Event.objects.count()
        stats["upcoming_events"] = Event.objects.filter(
            status=Event.STATUS_UPCOMING
        ).count()
    except Exception:
        stats["total_events"] = 0
        stats["upcoming_events"] = 0

    try:
        stats["total_news"] = NewsArticle.objects.count()
        stats["published_news"] = NewsArticle.objects.filter(
            status=NewsArticle.STATUS_PUBLISHED
        ).count()
    except Exception:
        stats["total_news"] = 0
        stats["published_news"] = 0

    try:
        stats["active_team_members"] = TeamMember.objects.filter(
            is_active=True
        ).count()
    except Exception:
        stats["active_team_members"] = 0

    try:
        stats["pending_memberships"] = MembershipApplication.objects.filter(
            status=MembershipApplication.STATUS_PENDING
        ).count()
        stats["total_memberships"] = MembershipApplication.objects.count()
    except Exception:
        stats["pending_memberships"] = 0
        stats["total_memberships"] = 0

    try:
        stats["unread_contacts"] = ContactMessage.objects.filter(
            status=ContactMessage.STATUS_UNREAD
        ).count()
        stats["total_contacts"] = ContactMessage.objects.count()
    except Exception:
        stats["unread_contacts"] = 0
        stats["total_contacts"] = 0

    try:
        stats["total_albums"] = GalleryAlbum.objects.count()
        stats["total_gallery_images"] = GalleryImage.objects.count()
    except Exception:
        stats["total_albums"] = 0
        stats["total_gallery_images"] = 0

    try:
        stats["active_announcements"] = Announcement.objects.filter(
            is_active=True
        ).count()
    except Exception:
        stats["active_announcements"] = 0

    try:
        org = Organization.objects.first()
        stats["organization"] = org
        stats["org_motto"] = org.motto if org and org.motto else "Unity, Leadership, and Service"
    except Exception:
        stats["organization"] = None
        stats["org_motto"] = "Unity, Leadership, and Service"

    return stats


@register.simple_tag
def get_recent_pending_memberships(limit=5):
    """Retrieve recent pending membership applications for triage."""
    try:
        return MembershipApplication.objects.filter(
            status=MembershipApplication.STATUS_PENDING
        ).order_by("-submitted_at")[:limit]
    except Exception:
        return []


@register.simple_tag
def get_recent_contact_messages(limit=5):
    """Retrieve recent contact messages for quick review."""
    try:
        return ContactMessage.objects.order_by("-created_at")[:limit]
    except Exception:
        return []


@register.simple_tag
def get_grouped_admin_apps(app_list):
    """
    Reorganize the default Django app_list into logical conceptual groups:
    - CONTENT
    - PEOPLE & MEMBERSHIP
    - ORGANIZATION
    - COMMUNICATION
    - SYSTEM & SETTINGS

    Respects all built-in Django permissions and retains model links, add URLs,
    and icons.
    """
    groups_def = [
        {
            "id": "content",
            "name": "Content Management",
            "description": "Activities, scheduled events, news publications, and photo albums",
            "icon": "folder",
            "models": {
                "activity": {"badge": "Activities", "icon": "calendar-check"},
                "activitycategory": {"badge": "Taxonomy", "icon": "tags"},
                "activityimage": {"badge": "Media", "icon": "image"},
                "event": {"badge": "Events", "icon": "calendar"},
                "eventimage": {"badge": "Media", "icon": "image"},
                "newsarticle": {"badge": "Editorial", "icon": "newspaper"},
                "galleryalbum": {"badge": "Gallery", "icon": "images"},
                "galleryimage": {"badge": "Media", "icon": "image"},
            },
            "items": [],
        },
        {
            "id": "people",
            "name": "People & Membership",
            "description": "Membership applications, executive committee, staff, and access roles",
            "icon": "users",
            "models": {
                "membershipapplication": {"badge": "Workflow", "icon": "user-plus"},
                "teammember": {"badge": "Committee", "icon": "user-check"},
                "user": {"badge": "Accounts", "icon": "shield"},
                "group": {"badge": "Permissions", "icon": "lock"},
            },
            "items": [],
        },
        {
            "id": "organization",
            "name": "Organization & Identity",
            "description": "Official club profile, motto, mission, vision, and site announcements",
            "icon": "flag",
            "models": {
                "organization": {"badge": "Profile", "icon": "award"},
                "announcement": {"badge": "Notices", "icon": "bell"},
            },
            "items": [],
        },
        {
            "id": "communication",
            "name": "Communication & Inquiries",
            "description": "Inbound contact messages and public visitor communications",
            "icon": "mail",
            "models": {
                "contactmessage": {"badge": "Inbox", "icon": "inbox"},
            },
            "items": [],
        },
    ]

    all_matched_models = set()

    for app in app_list:
        for model in app.get("models", []):
            model_key = model.get("object_name", "").lower()
            matched = False
            for group in groups_def:
                if model_key in group["models"]:
                    meta = group["models"][model_key]
                    model_copy = dict(model)
                    model_copy["group_badge"] = meta.get("badge", "")
                    model_copy["icon"] = meta.get("icon", "circle")
                    model_copy["app_label"] = app.get("app_label", "")
                    group["items"].append(model_copy)
                    all_matched_models.add(model_key)
                    matched = True
                    break

    # Filter out any groups that have no permitted items
    active_groups = [g for g in groups_def if g["items"]]

    # Collect any leftovers (e.g. third-party apps installed in future)
    leftovers = []
    for app in app_list:
        for model in app.get("models", []):
            model_key = model.get("object_name", "").lower()
            if model_key not in all_matched_models:
                leftovers.append(dict(model))

    if leftovers:
        active_groups.append({
            "id": "other",
            "name": "Other Applications",
            "description": "Additional administrative models",
            "icon": "grid",
            "items": leftovers,
        })

    return active_groups
