from django.test import TestCase
from rest_framework.test import APITestCase

from .models import TeamMember


class TeamMemberModelTests(TestCase):
    def test_members_are_ordered_by_display_order_then_name(self):
        TeamMember.objects.create(name="Bina", position="Secretary", display_order=2)
        first = TeamMember.objects.create(
            name="Anil", position="President", display_order=1
        )

        self.assertEqual(TeamMember.objects.first(), first)
        self.assertTrue(first.is_active)


class TeamMemberApiTests(APITestCase):
    def test_only_active_members_are_visible_in_display_order(self):
        TeamMember.objects.create(name="Second", position="Member", display_order=2)
        TeamMember.objects.create(name="First", position="President", display_order=1)
        TeamMember.objects.create(
            name="Inactive", position="Former", display_order=0, is_active=False
        )

        response = self.client.get("/api/team/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            [member["name"] for member in response.data], ["First", "Second"]
        )
        self.assertNotIn("phone", response.data[0])
