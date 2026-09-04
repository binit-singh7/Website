from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import NewsArticle
from .serializers import NewsArticleDetailSerializer, NewsArticleListSerializer


class NewsArticleListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = NewsArticleListSerializer

    def get_queryset(self):
        queryset = NewsArticle.objects.filter(status=NewsArticle.STATUS_PUBLISHED)
        year = self.request.query_params.get("year")
        if year and year.isdigit():
            queryset = queryset.filter(published_at__year=year)
        return queryset


class NewsArticleDetailView(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = NewsArticleDetailSerializer
    lookup_field = "slug"
    queryset = NewsArticle.objects.filter(status=NewsArticle.STATUS_PUBLISHED)
