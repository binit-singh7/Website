from django import forms
from django.contrib import admin
from django.db.models import Count, Max
from django.utils.html import format_html

from core.validators import image_upload_validators

from .models import GalleryAlbum, GalleryImage


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    widget = MultipleFileInput

    def clean(self, data, initial=None):
        if not data:
            return []

        files = data if isinstance(data, (list, tuple)) else [data]
        clean_file = super().clean
        return [clean_file(uploaded_file, initial) for uploaded_file in files]


class GalleryAlbumAdminForm(forms.ModelForm):
    batch_images = MultipleFileField(
        required=False,
        validators=image_upload_validators,
        label="Batch Upload Images (Select Multiple Files)",
        help_text="Upload multiple photos simultaneously into this album. They will automatically append with sequential display orders.",
        widget=MultipleFileInput(attrs={"multiple": True}),
    )

    class Meta:
        model = GalleryAlbum
        fields = "__all__"


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 0
    fields = ("image_thumbnail", "image", "caption", "display_order")
    readonly_fields = ("image_thumbnail",)

    @admin.display(description="Preview")
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" class="ayc-thumb" alt="{}" />',
                obj.image.url,
                obj.caption or "Album image",
            )
        return format_html('<span class="ayc-thumb-placeholder">—</span>')


@admin.register(GalleryAlbum)
class GalleryAlbumAdmin(admin.ModelAdmin):
    form = GalleryAlbumAdminForm
    inlines = (GalleryImageInline,)
    list_display = (
        "cover_thumbnail",
        "title",
        "date",
        "image_count",
        "published_badge",
    )
    list_filter = ("is_published",)
    search_fields = ("title", "description")
    ordering = ("-date",)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at", "cover_preview")

    fieldsets = (
        (
            "Album Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "date",
                    "description",
                ),
            },
        ),
        (
            "Cover Media & Status",
            {
                "fields": (
                    "cover_image",
                    "cover_preview",
                    "is_published",
                ),
            },
        ),
        (
            "Batch Photo Upload",
            {
                "fields": ("batch_images",),
                "description": "Select multiple image files at once to append them to this album upon save.",
            },
        ),
        (
            "Timestamps",
            {
                "fields": ("created_at", "updated_at"),
                "classes": ("collapse",),
            },
        ),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            _image_count=Count("images")
        )

    @admin.display(description="Photos", ordering="_image_count")
    def image_count(self, obj):
        count = getattr(obj, "_image_count", 0)
        return format_html(
            '<span class="ayc-badge ayc-badge--neutral">{} photo{}</span>',
            count,
            "s" if count != 1 else "",
        )

    @admin.display(description="Cover")
    def cover_thumbnail(self, obj):
        if obj.cover_image:
            return format_html(
                '<img src="{}" class="ayc-thumb" alt="{}" />',
                obj.cover_image.url,
                obj.title,
            )
        return format_html('<span class="ayc-thumb-placeholder">No Cover</span>')

    @admin.display(description="Cover Preview")
    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html(
                '<div class="ayc-thumb-preview-container">'
                '<img src="{}" class="ayc-thumb-preview-img" alt="{}" />'
                '<div class="ayc-thumb-preview-info">'
                '<strong>Album Cover Preview</strong><br>'
                'Path: {}'
                '</div>'
                '</div>',
                obj.cover_image.url,
                obj.title,
                obj.cover_image.name,
            )
        return format_html('<span style="color: var(--ayc-text-muted);">No cover image uploaded.</span>')

    @admin.display(description="Status", ordering="is_published")
    def published_badge(self, obj):
        if obj.is_published:
            return format_html(
                '<span class="ayc-badge ayc-badge--success"><span class="ayc-badge-dot"></span>Published</span>'
            )
        return format_html(
            '<span class="ayc-badge ayc-badge--neutral"><span class="ayc-badge-dot"></span>Draft</span>'
        )

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)

        uploaded_files = request.FILES.getlist("batch_images")
        if not uploaded_files:
            return

        current_order = GalleryImage.objects.filter(album=form.instance).aggregate(
            max_order=Max("display_order")
        )["max_order"]
        next_order = 0 if current_order is None else current_order + 1

        for uploaded_file in uploaded_files:
            GalleryImage.objects.create(
                album=form.instance,
                image=uploaded_file,
                display_order=next_order,
            )
            next_order += 1


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("image_thumbnail", "album", "caption", "display_order", "created_at")
    list_filter = ("album",)
    search_fields = ("album__title", "caption")
    ordering = ("album", "display_order")
    readonly_fields = ("created_at", "image_preview")

    fieldsets = (
        (
            "Image Details",
            {
                "fields": ("album", "image", "image_preview", "caption", "display_order"),
            },
        ),
        (
            "Timestamp",
            {
                "fields": ("created_at",),
                "classes": ("collapse",),
            },
        ),
    )

    @admin.display(description="Thumbnail")
    def image_thumbnail(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" class="ayc-thumb" alt="{}" />',
                obj.image.url,
                obj.caption or "Photo",
            )
        return format_html('<span class="ayc-thumb-placeholder">—</span>')

    @admin.display(description="Preview")
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<div class="ayc-thumb-preview-container">'
                '<img src="{}" class="ayc-thumb-preview-img" alt="{}" />'
                '<div class="ayc-thumb-preview-info">'
                '<strong>Photo Preview</strong><br>'
                'Path: {}'
                '</div>'
                '</div>',
                obj.image.url,
                obj.caption or "Photo",
                obj.image.name,
            )
        return format_html('<span style="color: var(--ayc-text-muted);">No image uploaded.</span>')
