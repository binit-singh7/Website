from django.contrib import admin
from django.utils.html import format_html

from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = (
        "photo_thumbnail",
        "name",
        "position",
        "display_order",
        "active_badge",
        "phone",
        "email",
    )
    list_filter = ("is_active",)
    search_fields = ("name", "position", "bio", "phone", "email")
    ordering = ("display_order", "name")
    readonly_fields = ("created_at", "updated_at", "photo_preview")

    fieldsets = (
        (
            "Leadership Profile",
            {
                "fields": (
                    "name",
                    "position",
                    "bio",
                    "photo",
                    "photo_preview",
                ),
                "description": "Executive committee member or club leadership profile.",
            },
        ),
        (
            "Display & Visibility",
            {
                "fields": (
                    "display_order",
                    "is_active",
                ),
                "description": "Control ordering on the public team page and active visibility.",
            },
        ),
        (
            "Contact Details",
            {
                "fields": (
                    "phone",
                    "email",
                ),
                "description": "Optional official contact info approved for communication.",
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

    @admin.display(description="Photo")
    def photo_thumbnail(self, obj):
        if obj.photo:
            return format_html(
                '<img src="{}" class="ayc-thumb" alt="{}" />',
                obj.photo.url,
                obj.name,
            )
        return format_html('<span class="ayc-thumb-placeholder">No Photo</span>')

    @admin.display(description="Photo Preview")
    def photo_preview(self, obj):
        if obj.photo:
            return format_html(
                '<div class="ayc-thumb-preview-container">'
                '<img src="{}" class="ayc-thumb-preview-img" alt="{}" />'
                '<div class="ayc-thumb-preview-info">'
                '<strong>Current Profile Photo</strong><br>'
                'Path: {}'
                '</div>'
                '</div>',
                obj.photo.url,
                obj.name,
                obj.photo.name,
            )
        return format_html('<span style="color: var(--ayc-text-muted);">No profile photo uploaded.</span>')

    @admin.display(description="Status", ordering="is_active")
    def active_badge(self, obj):
        if obj.is_active:
            return format_html(
                '<span class="ayc-badge ayc-badge--success"><span class="ayc-badge-dot"></span>Active</span>'
            )
        return format_html(
            '<span class="ayc-badge ayc-badge--neutral"><span class="ayc-badge-dot"></span>Inactive</span>'
        )
