from django.urls import path

from .views import MembershipApplicationCreateView

urlpatterns = [
    path(
        "membership/apply/",
        MembershipApplicationCreateView.as_view(),
        name="membership-apply",
    ),
]
