from django.contrib import admin
from django.utils.html import format_html

from .models import Announcement, Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = (
        "logo_thumbnail",
        "name",
        "short_name",
        "motto_display",
        "phone",
        "email",
        "updated_at",
    )
    search_fields = ("name", "short_name", "motto", "description")
    readonly_fields = ("created_at", "updated_at", "logo_preview")

    fieldsets = (
        (
            "Club Identity",
            {
                "fields": (
                    "name",
                    "short_name",
                    "motto",
                    "logo",
                    "logo_preview",
                    "description",
                ),
                "description": "Official branding and public organization identity.",
            },
        ),
        (
            "Mission & Vision",
            {
                "fields": ("vision", "mission"),
            },
        ),
        (
            "Contact & Location",
            {
                "fields": ("phone", "email", "address"),
            },
        ),
        (
            "Social Media Channels",
            {
                "fields": (
                    "facebook_url",
                    "instagram_url",
                    "youtube_url",
                    "tiktok_url",
                ),
            },
        ),
        (
            "System Timestamps",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )

    @admin.display(description="Logo")
    def logo_thumbnail(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" class="ayc-thumb" alt="{} logo" />',
                obj.logo.url,
                obj.short_name or obj.name,
            )
        return format_html('<span class="ayc-thumb-placeholder">No Logo</span>')

    @admin.display(description="Logo Preview")
    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<div class="ayc-thumb-preview-container">'
                '<img src="{}" class="ayc-thumb-preview-img" alt="Logo preview" />'
                '<div class="ayc-thumb-preview-info">'
                '<strong>Current Logo</strong><br>'
                'Format: {}<br>'
                'Path: {}'
                '</div>'
                '</div>',
                obj.logo.url,
                obj.logo.name.split(".")[-1].upper(),
                obj.logo.name,
            )
        return format_html('<span style="color: var(--ayc-text-muted);">No club logo uploaded yet.</span>')

    @admin.display(description="Official Motto")
    def motto_display(self, obj):
        motto = obj.motto or "Unity, Leadership, and Service"
        return format_html(
            '<span style="font-weight: 600; color: var(--ayc-primary-dark);">{}</span>',
            motto,
        )


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "priority_badge",
        "active_badge",
        "start_date",
        "end_date",
        "created_at",
    )
    list_filter = ("priority", "is_active")
    search_fields = ("title", "content")
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        (
            "Announcement Content",
            {
                "fields": ("title", "content", "priority", "is_active"),
            },
        ),
        (
            "Display Schedule",
            {
                "fields": ("start_date", "end_date"),
                "description": "Optional active date window for this announcement.",
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )

    @admin.display(description="Priority", ordering="priority")
    def priority_badge(self, obj):
        badge_classes = {
            Announcement.PRIORITY_URGENT: "ayc-badge--danger",
            Announcement.PRIORITY_IMPORTANT: "ayc-badge--warning",
            Announcement.PRIORITY_NORMAL: "ayc-badge--info",
        }
        css_class = badge_classes.get(obj.priority, "ayc-badge--neutral")
        return format_html(
            '<span class="ayc-badge {}"><span class="ayc-badge-dot"></span>{}</span>',
            css_class,
            obj.get_priority_display(),
        )

    @admin.display(description="Status", ordering="is_active")
    def active_badge(self, obj):
        if obj.is_active:
            return format_html(
                '<span class="ayc-badge ayc-badge--success"><span class="ayc-badge-dot"></span>Active</span>'
            )
        return format_html(
            '<span class="ayc-badge ayc-badge--neutral"><span class="ayc-badge-dot"></span>Inactive</span>'
        )
