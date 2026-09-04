from django.contrib.auth import get_user_model
from django.test import TestCase

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
