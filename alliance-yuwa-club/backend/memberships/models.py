from django.conf import settings
from django.db import models


class MembershipApplication(models.Model):
    STATUS_PENDING = "pending"
    STATUS_APPROVED = "approved"
    STATUS_REJECTED = "rejected"
    STATUS_CHOICES = [
        (STATUS_PENDING, "Pending"),
        (STATUS_APPROVED, "Approved"),
        (STATUS_REJECTED, "Rejected"),
    ]

    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    address = models.TextField()
    ward = models.CharField(max_length=50)
    occupation = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    areas_of_interest = models.TextField()
    reason_for_joining = models.TextField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STATUS_PENDING, db_index=True
    )
    submitted_at = models.DateTimeField(auto_now_add=True, db_index=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)
    reviewed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="reviewed_membership_applications",
    )
    admin_notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-submitted_at"]

    def __str__(self):
        return self.full_name
