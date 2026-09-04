from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APITestCase

from .models import NewsArticle


class NewsArticleModelTests(TestCase):
    def test_author_is_set_to_null_when_user_is_deleted(self):
        user = get_user_model().objects.create_user(
            username="editor", password="test-password"
        )
        article = NewsArticle.objects.create(
            title="Convention Update",
            slug="convention-update",
            content="Update",
            author=user,
        )

        user.delete()
        article.refresh_from_db()

        self.assertIsNone(article.author)
        self.assertEqual(article.status, NewsArticle.STATUS_DRAFT)


class NewsArticleApiTests(APITestCase):
    def setUp(self):
        self.article = NewsArticle.objects.create(
            title="Published News",
            slug="published-news",
            excerpt="Visible",
            content="Full content",
            status=NewsArticle.STATUS_PUBLISHED,
            published_at=timezone.now(),
        )
        NewsArticle.objects.create(
            title="Draft News",
            slug="draft-news",
            content="Hidden",
        )

    def test_list_filters_year_and_paginates_without_unpublished_articles(self):
        response = self.client.get(f"/api/news/?year={timezone.now().year}&page_size=1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["count"], 1)
        self.assertEqual(response.data["results"][0]["slug"], self.article.slug)

    def test_detail_returns_published_article_and_hides_draft(self):
        response = self.client.get("/api/news/published-news/")
        draft_response = self.client.get("/api/news/draft-news/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["content"], "Full content")
        self.assertEqual(draft_response.status_code, 404)
