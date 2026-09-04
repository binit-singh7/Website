from django.urls import path

from .views import AnnouncementListView, OrganizationView

urlpatterns = [
    path("organization/", OrganizationView.as_view(), name="organization"),
    path("announcements/", AnnouncementListView.as_view(), name="announcement-list"),
]
