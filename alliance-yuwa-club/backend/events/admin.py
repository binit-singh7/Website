from django.contrib import admin
from django.utils.html import format_html

from .models import Event, EventImage


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 1
    fields = ("image_thumbnail", "image", "caption", "display_order")
    readonly_fields = ("image_thumbnail",)

    @admin.display(description="Preview")
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" class="ayc-thumb" alt="{}" />',
                obj.image.url,
                obj.caption or "Event photo",
            )
        return format_html('<span class="ayc-thumb-placeholder">—</span>')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = (EventImageInline,)
    list_display = (
        "cover_thumbnail",
        "title",
        "start_datetime",
        "status_badge",
        "registration_badge",
        "featured_badge",
    )
    list_filter = ("status", "featured", "registration_required")
    search_fields = ("title", "description", "location")
    ordering = ("start_datetime",)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at", "cover_preview")

    fieldsets = (
        (
            "Event Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "description",
                    "location",
                ),
            },
        ),
        (
            "Schedule & Timing",
            {
                "fields": ("start_datetime", "end_datetime"),
            },
        ),
        (
            "Participation & Registration",
            {
                "fields": (
                    "status",
                    "featured",
                    "registration_required",
                    "registration_url",
                ),
            },
        ),
        (
            "Visual Media",
            {
                "fields": (
                    "cover_image",
                    "cover_preview",
                ),
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

    @admin.display(description="Cover")
    def cover_thumbnail(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" class="ayc-thumb" alt="{}" />',
                obj.cover_image.url,
                obj.title,
            )
        return format_html('<span class="ayc-thumb-placeholder">No Img</span>')

    @admin.display(description="Cover Preview")
    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<div class="ayc-thumb-preview-container">'
                '<img src="{}" class="ayc-thumb-preview-img" alt="{}" />'
                '<div class="ayc-thumb-preview-info">'
                '<strong>Event Cover Preview</strong><br>'
                'Path: {}'
                '</div>'
                '</div>',
                obj.cover_image.url,
                obj.title,
                obj.cover_image.name,
            )
        return format_html('<span style="color: var(--ayc-text-muted);">No cover image uploaded.</span>')

    @admin.display(description="Status", ordering="status")
    def status_badge(self, obj):
        badge_classes = {
            Event.STATUS_UPCOMING: "ayc-badge--warning",
            Event.STATUS_ONGOING: "ayc-badge--info",
            Event.STATUS_COMPLETED: "ayc-badge--success",
            Event.STATUS_CANCELLED: "ayc-badge--danger",
            Event.STATUS_DRAFT: "ayc-badge--neutral",
        }
        css_class = badge_classes.get(obj.status, "ayc-badge--neutral")
        return format_html(
            '<span class="ayc-badge {}"><span class="ayc-badge-dot"></span>{}</span>',
            css_class,
            obj.get_status_display(),
        )

    @admin.display(description="Registration", ordering="registration_required")
    def registration_badge(self, obj):
        if obj.registration_required:
            return format_html(
                '<span class="ayc-badge ayc-badge--info">Required</span>'
            )
        return format_html('<span style="color: var(--ayc-text-muted);">Open</span>')

    @admin.display(description="Featured", ordering="featured")
    def featured_badge(self, obj):
        if obj.featured:
            return format_html(
                '<span class="ayc-badge ayc-badge--success">★ Featured</span>'
            )
        return format_html('<span style="color: var(--ayc-text-muted);">—</span>')


@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    list_display = ("image_thumbnail", "event", "caption", "display_order", "created_at")
    list_filter = ("event",)
    search_fields = ("event__title", "caption")
    ordering = ("event", "display_order")
    readonly_fields = ("created_at",)

    @admin.display(description="Thumbnail")
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" class="ayc-thumb" alt="{}" />',
                obj.image.url,
                obj.caption or "Photo",
            )
        return format_html('<span class="ayc-thumb-placeholder">—</span>')
