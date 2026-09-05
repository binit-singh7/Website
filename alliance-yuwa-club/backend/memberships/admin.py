from django.contrib import admin, messages
from django.utils import timezone

from .emails import (
    send_application_approved_email,
    send_application_rejected_email,
)
from .models import MembershipApplication


@admin.register(MembershipApplication)
class MembershipApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "phone",
        "status",
        "submitted_at",
        "reviewed_at",
        "reviewed_by",
    )
    list_filter = ("status",)
    search_fields = ("full_name", "email", "phone", "ward")
    ordering = ("-submitted_at",)
    readonly_fields = ("submitted_at", "reviewed_at", "reviewed_by")
    actions = ("approve_applications", "reject_applications")

    @admin.action(description="Approve selected membership applications")
    def approve_applications(self, request, queryset):
        self._review_applications(
            request,
            queryset,
            MembershipApplication.STATUS_APPROVED,
            send_application_approved_email,
            "approved",
        )

    @admin.action(description="Reject selected membership applications")
    def reject_applications(self, request, queryset):
        self._review_applications(
            request,
            queryset,
            MembershipApplication.STATUS_REJECTED,
            send_application_rejected_email,
            "rejected",
        )

    def _review_applications(
        self, request, queryset, status_value, send_notification, label
    ):
        changed_count = 0
        failed_email_count = 0

        for application in queryset.exclude(status=status_value):
            application.status = status_value
            application.reviewed_at = timezone.now()
            application.reviewed_by = request.user
            application.save(update_fields=("status", "reviewed_at", "reviewed_by"))
            changed_count += 1
            if not send_notification(application):
                failed_email_count += 1

        self.message_user(
            request,
            f"{changed_count} application(s) marked {label}.",
            messages.SUCCESS,
        )
        if failed_email_count:
            self.message_user(
                request,
                f"{failed_email_count} status email(s) could not be delivered.",
                messages.WARNING,
            )
