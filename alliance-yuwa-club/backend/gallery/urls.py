from django.urls import path

from .views import GalleryAlbumDetailView, GalleryAlbumListView

urlpatterns = [
    path("gallery/albums/", GalleryAlbumListView.as_view(), name="gallery-album-list"),
    path(
        "gallery/albums/<slug:slug>/",
        GalleryAlbumDetailView.as_view(),
        name="gallery-album-detail",
    ),
]
