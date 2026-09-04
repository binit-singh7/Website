from django.contrib import admin

from .models import MembershipApplication


@admin.register(MembershipApplication)
class MembershipApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "phone",
        "status",
        "submitted_at",
        "reviewed_by",
    )
    list_filter = ("status",)
    search_fields = ("full_name", "email", "phone", "ward")
    ordering = ("-submitted_at",)
    readonly_fields = ("submitted_at",)
