from django.contrib import admin

from .models import Activity, ActivityCategory, ActivityImage


@admin.register(ActivityCategory)
class ActivityCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "updated_at")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "date", "status", "featured")
    list_filter = ("status", "featured", "category")
    search_fields = ("title", "description", "location")
    ordering = ("-date",)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")


@admin.register(ActivityImage)
class ActivityImageAdmin(admin.ModelAdmin):
    list_display = ("activity", "caption", "display_order", "created_at")
    list_filter = ("activity",)
    search_fields = ("activity__title", "caption")
    ordering = ("activity", "display_order")
    readonly_fields = ("created_at",)
