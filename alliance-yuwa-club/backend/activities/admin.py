from django.contrib import admin
from django.db.models import Count
from django.utils.html import format_html

from .models import Activity, ActivityCategory, ActivityImage


class ActivityImageInline(admin.TabularInline):
    model = ActivityImage
    extra = 1
    fields = ("image_thumbnail", "image", "caption", "display_order")
    readonly_fields = ("image_thumbnail",)

    @admin.display(description="Preview")
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" class="ayc-thumb" alt="{}" />',
                obj.image.url,
                obj.caption or "Activity photo",
            )
        return format_html('<span class="ayc-thumb-placeholder">—</span>')


@admin.register(ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "activity_count", "updated_at")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            _activity_count=Count("activities")
        )

    @admin.display(description="Total Activities", ordering="_activity_count")
    def activity_count(self, obj):
        count = getattr(obj, "_activity_count", 0)
        return format_html(
            '<span class="ayc-badge ayc-badge--neutral">{} program{}</span>',
            count,
            "s" if count != 1 else "",
        )


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    inlines = (ActivityImageInline,)
    list_display = (
        "cover_thumbnail",
        "title",
        "category",
        "date",
        "status_badge",
        "featured_badge",
    )
    list_filter = ("status", "featured", "category")
    search_fields = ("title", "description", "location")
    ordering = ("-date",)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at", "cover_preview")
    autocomplete_fields = ()

    fieldsets = (
        (
            "Program Details",
            {
                "fields": (
                    "title",
                    "slug",
                    "category",
                    "date",
                    "location",
                ),
                "description": "Core information about the club activity or community program.",
            },
        ),
        (
            "Activity Description & Report",
            {
                "fields": ("description",),
            },
        ),
        (
            "Cover Image & Visibility",
            {
                "fields": (
                    "cover_image",
                    "cover_preview",
                    "status",
                    "featured",
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
                '<strong>Cover Image Preview</strong><br>'
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
            Activity.STATUS_PUBLISHED: "ayc-badge--success",
            Activity.STATUS_DRAFT: "ayc-badge--warning",
            Activity.STATUS_ARCHIVED: "ayc-badge--neutral",
        }
        css_class = badge_classes.get(obj.status, "ayc-badge--neutral")
        return format_html(
            '<span class="ayc-badge {}"><span class="ayc-badge-dot"></span>{}</span>',
            css_class,
            obj.get_status_display(),
        )

    @admin.display(description="Featured", ordering="featured")
    def featured_badge(self, obj):
        if obj.featured:
            return format_html(
                '<span class="ayc-badge ayc-badge--success">★ Featured</span>'
            )
        return format_html('<span style="color: var(--ayc-text-muted);">—</span>')


@admin.register(ActivityImage)
class ActivityImageAdmin(admin.ModelAdmin):
    list_display = ("image_thumbnail", "activity", "caption", "display_order", "created_at")
    list_filter = ("activity",)
    search_fields = ("activity__title", "caption")
    ordering = ("activity", "display_order")
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
