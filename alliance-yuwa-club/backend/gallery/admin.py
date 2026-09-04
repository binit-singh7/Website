from django.contrib import admin
from django import forms
from django.db.models import Max

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
        label="Batch Upload Images (Select Multiple Files)",
        widget=MultipleFileInput(attrs={"multiple": True}),
    )

    class Meta:
        model = GalleryAlbum
        fields = "__all__"


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 0
    fields = ("image", "caption", "display_order")


@admin.register(GalleryAlbum)
class GalleryAlbumAdmin(admin.ModelAdmin):
    form = GalleryAlbumAdminForm
    inlines = (GalleryImageInline,)
    list_display = ("title", "date", "is_published")
    list_filter = ("is_published",)
    search_fields = ("title", "description")
    ordering = ("-date",)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")

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
    list_display = ("album", "caption", "display_order", "created_at")
    list_filter = ("album",)
    search_fields = ("album__title", "caption")
    ordering = ("album", "display_order")
    readonly_fields = ("created_at",)
