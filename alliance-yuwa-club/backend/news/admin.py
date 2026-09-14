from django.contrib import admin
from django.utils.html import format_html

from .models import NewsArticle


@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = (
        "featured_image_thumbnail",
        "title",
        "author",
        "status_badge",
        "published_at",
    )
    list_filter = ("status",)
    search_fields = ("title", "excerpt", "content")
    ordering = ("-published_at",)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at", "featured_image_preview")
    autocomplete_fields = ("author",)

    fieldsets = (
        (
            "Article Content",
            {
                "fields": (
                    "title",
                    "slug",
                    "excerpt",
                    "content",
                ),
            },
        ),
        (
            "Authorship & Publishing",
            {
                "fields": (
                    "author",
                    "status",
                    "published_at",
                ),
            },
        ),
        (
            "Featured Media",
            {
                "fields": (
                    "featured_image",
                    "featured_image_preview",
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

    @admin.display(description="Image")
    def featured_image_thumbnail(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" class="ayc-thumb" alt="{}" />',
                obj.featured_image.url,
                obj.title,
            )
        return format_html('<span class="ayc-thumb-placeholder">No Img</span>')

    @admin.display(description="Featured Image Preview")
    def featured_image_preview(self, obj):
        if obj.featured_image:
            return format_html(
                '<div class="ayc-thumb-preview-container">'
                '<img src="{}" class="ayc-thumb-preview-img" alt="{}" />'
                '<div class="ayc-thumb-preview-info">'
                '<strong>Featured Article Image</strong><br>'
                'Path: {}'
                '</div>'
                '</div>',
                obj.featured_image.url,
                obj.title,
                obj.featured_image.name,
            )
        return format_html('<span style="color: var(--ayc-text-muted);">No featured image uploaded.</span>')

    @admin.display(description="Status", ordering="status")
    def status_badge(self, obj):
        badge_classes = {
            NewsArticle.STATUS_PUBLISHED: "ayc-badge--success",
            NewsArticle.STATUS_DRAFT: "ayc-badge--warning",
            NewsArticle.STATUS_ARCHIVED: "ayc-badge--neutral",
        }
        css_class = badge_classes.get(obj.status, "ayc-badge--neutral")
        return format_html(
            '<span class="ayc-badge {}"><span class="ayc-badge-dot"></span>{}</span>',
            css_class,
            obj.get_status_display(),
        )
