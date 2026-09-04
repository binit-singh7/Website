from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import TeamMember
from .serializers import TeamMemberSerializer


class TeamMemberListView(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = TeamMemberSerializer
    pagination_class = None
    queryset = TeamMember.objects.filter(is_active=True)
