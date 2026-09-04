from django.urls import path

from .views import ActivityCategoryListView, ActivityDetailView, ActivityListView

urlpatterns = [
    path(
        "activity-categories/",
        ActivityCategoryListView.as_view(),
        name="activity-category-list",
    ),
    path("activities/", ActivityListView.as_view(), name="activity-list"),
    path(
        "activities/<slug:slug>/", ActivityDetailView.as_view(), name="activity-detail"
    ),
]
