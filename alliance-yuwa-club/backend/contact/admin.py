from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "name", "email", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("name", "email", "subject", "message")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")
