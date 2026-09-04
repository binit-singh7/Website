from django.urls import path

from .views import NewsArticleDetailView, NewsArticleListView

urlpatterns = [
    path("news/", NewsArticleListView.as_view(), name="news-list"),
    path("news/<slug:slug>/", NewsArticleDetailView.as_view(), name="news-detail"),
]
