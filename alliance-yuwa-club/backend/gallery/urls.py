from django.urls import path

from .views import (
    ActivityGalleryDetailView,
    ActivityGalleryListView,
    GalleryAlbumDetailView,
    GalleryAlbumListView,
)

urlpatterns = [
    # Manual gallery albums (existing)
    path("gallery/albums/", GalleryAlbumListView.as_view(), name="gallery-album-list"),
    path(
        "gallery/albums/<slug:slug>/",
        GalleryAlbumDetailView.as_view(),
        name="gallery-album-detail",
    ),

    # Activity images surfaced as virtual gallery albums (new)
    # These endpoints derive data live from published Activity records —
    # no Gallery DB records are written, no files are duplicated.
    path(
        "gallery/activity-images/",
        ActivityGalleryListView.as_view(),
        name="gallery-activity-list",
    ),
    path(
        "gallery/activity-images/<slug:slug>/",
        ActivityGalleryDetailView.as_view(),
        name="gallery-activity-detail",
    ),
]
