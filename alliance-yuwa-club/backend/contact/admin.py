from django.contrib import admin, messages
from django.utils.html import format_html

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = (
        "subject",
        "name",
        "email",
        "phone",
        "status_badge",
        "created_at",
    )
    list_filter = ("status",)
    search_fields = ("name", "email", "subject", "message", "phone")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
    actions = ("mark_as_read", "mark_as_replied", "mark_as_archived")

    fieldsets = (
        (
            "Sender Details",
            {
                "fields": (
                    "name",
                    "email",
                    "phone",
                    "subject",
                ),
            },
        ),
        (
            "Message Body",
            {
                "fields": ("message",),
            },
        ),
        (
            "Inquiry Status",
            {
                "fields": ("status",),
                "description": "Track the review and response status of this visitor inquiry.",
            },
        ),
        (
            "Submission Timestamps",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )

    @admin.display(description="Status", ordering="status")
    def status_badge(self, obj):
        badge_classes = {
            ContactMessage.STATUS_UNREAD: "ayc-badge--danger",
            ContactMessage.STATUS_READ: "ayc-badge--neutral",
            ContactMessage.STATUS_REPLIED: "ayc-badge--info",
            ContactMessage.STATUS_ARCHIVED: "ayc-badge--neutral",
        }
        css_class = badge_classes.get(obj.status, "ayc-badge--neutral")
        return format_html(
            '<span class="ayc-badge {}"><span class="ayc-badge-dot"></span>{}</span>',
            css_class,
            obj.get_status_display(),
        )

    @admin.action(description="Mark selected messages as Read")
    def mark_as_read(self, request, queryset):
        updated = queryset.update(status=ContactMessage.STATUS_READ)
        self.message_user(
            request, f"{updated} message(s) marked as read.", messages.SUCCESS
        )

    @admin.action(description="Mark selected messages as Replied")
    def mark_as_replied(self, request, queryset):
        updated = queryset.update(status=ContactMessage.STATUS_REPLIED)
        self.message_user(
            request, f"{updated} message(s) marked as replied.", messages.SUCCESS
        )

    @admin.action(description="Mark selected messages as Archived")
    def mark_as_archived(self, request, queryset):
        updated = queryset.update(status=ContactMessage.STATUS_ARCHIVED)
        self.message_user(
            request, f"{updated} message(s) archived.", messages.SUCCESS
        )
