from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle

from .serializers import MembershipApplicationSerializer


class MembershipApplicationCreateView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = MembershipApplicationSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = "membership_application"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Membership application submitted successfully."},
            status=status.HTTP_201_CREATED,
        )
