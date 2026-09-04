from django.test import TestCase

from .models import TeamMember


class TeamMemberModelTests(TestCase):
    def test_members_are_ordered_by_display_order_then_name(self):
        TeamMember.objects.create(name="Bina", position="Secretary", display_order=2)
        first = TeamMember.objects.create(
            name="Anil", position="President", display_order=1
        )

        self.assertEqual(TeamMember.objects.first(), first)
        self.assertTrue(first.is_active)
