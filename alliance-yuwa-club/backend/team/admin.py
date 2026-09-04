from django.contrib import admin

from .models import TeamMember


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "display_order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name", "position", "bio")
    ordering = ("display_order", "name")
    readonly_fields = ("created_at", "updated_at")
