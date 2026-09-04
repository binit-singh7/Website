from django.contrib import admin

from .models import Event, EventImage


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "start_datetime",
        "status",
        "featured",
        "registration_required",
    )
    list_filter = ("status", "featured", "registration_required")
    search_fields = ("title", "description", "location")
    ordering = ("start_datetime",)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")


@admin.register(EventImage)
class EventImageAdmin(admin.ModelAdmin):
    list_display = ("event", "caption", "display_order", "created_at")
    list_filter = ("event",)
    search_fields = ("event__title", "caption")
    ordering = ("event", "display_order")
    readonly_fields = ("created_at",)
