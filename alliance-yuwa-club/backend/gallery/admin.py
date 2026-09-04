from django.contrib import admin

from .models import GalleryAlbum, GalleryImage


@admin.register(GalleryAlbum)
class GalleryAlbumAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title", "description")
    ordering = ("-date",)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("album", "caption", "display_order", "created_at")
    list_filter = ("album",)
    search_fields = ("album__title", "caption")
    ordering = ("album", "display_order")
    readonly_fields = ("created_at",)
