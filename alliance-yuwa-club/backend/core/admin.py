from django.contrib import admin

from .models import Announcement, Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "short_name", "phone", "email", "updated_at")
    search_fields = ("name", "short_name")
    readonly_fields = ("created_at", "updated_at")


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "priority", "is_active", "start_date", "end_date")
    list_filter = ("priority", "is_active")
    search_fields = ("title", "content")
    readonly_fields = ("created_at", "updated_at")
