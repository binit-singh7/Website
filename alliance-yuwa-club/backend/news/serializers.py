from rest_framework import serializers

from .models import NewsArticle


class NewsArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsArticle
        fields = ("id", "title", "slug", "excerpt", "featured_image", "published_at")


class NewsArticleDetailSerializer(NewsArticleListSerializer):
    class Meta(NewsArticleListSerializer.Meta):
        fields = NewsArticleListSerializer.Meta.fields + ("content",)
