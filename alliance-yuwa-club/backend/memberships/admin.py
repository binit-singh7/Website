from django.contrib import admin, messages
from django.utils import timezone
from django.utils.html import format_html

from .emails import (
    send_application_approved_email,
    send_application_rejected_email,
)
from .models import MembershipApplication


@admin.register(MembershipApplication)
class MembershipApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "phone",
        "email",
        "ward",
        "status_badge",
        "submitted_at",
        "reviewed_at",
        "reviewed_by",
    )
    list_filter = ("status", "ward")
    search_fields = ("full_name", "email", "phone", "ward", "occupation")
    ordering = ("-submitted_at",)
    readonly_fields = ("submitted_at", "reviewed_at", "reviewed_by")
    actions = ("approve_applications", "reject_applications")

    fieldsets = (
        (
            "Applicant Profile",
            {
                "fields": (
                    "full_name",
                    "date_of_birth",
                    "phone",
                    "email",
                ),
            },
        ),
        (
            "Residence & Background",
            {
                "fields": (
                    "address",
                    "ward",
                    "occupation",
                    "education",
                ),
            },
        ),
        (
            "Application Statement",
            {
                "fields": (
                    "areas_of_interest",
                    "reason_for_joining",
                ),
            },
        ),
        (
            "Administrative Review & Decision",
            {
                "fields": (
                    "status",
                    "reviewed_by",
                    "reviewed_at",
                    "admin_notes",
                ),
                "description": "Authorized staff review. Use actions to approve/reject with applicant email notification.",
            },
        ),
        (
            "Submission Timestamp",
            {
                "fields": ("submitted_at",),
                "classes": ("collapse",),
            },
        ),
    )

    @admin.display(description="Status", ordering="status")
    def status_badge(self, obj):
        badge_classes = {
            MembershipApplication.STATUS_PENDING: "ayc-badge--warning",
            MembershipApplication.STATUS_APPROVED: "ayc-badge--success",
            MembershipApplication.STATUS_REJECTED: "ayc-badge--danger",
        }
        css_class = badge_classes.get(obj.status, "ayc-badge--neutral")
        return format_html(
            '<span class="ayc-badge {}"><span class="ayc-badge-dot"></span>{}</span>',
            css_class,
            obj.get_status_display(),
        )

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
