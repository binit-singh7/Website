from django.db import models


class ContactMessage(models.Model):
    STATUS_UNREAD = "unread"
    STATUS_READ = "read"
    STATUS_REPLIED = "replied"
    STATUS_ARCHIVED = "archived"
    STATUS_CHOICES = [
        (STATUS_UNREAD, "Unread"),
        (STATUS_READ, "Read"),
        (STATUS_REPLIED, "Replied"),
        (STATUS_ARCHIVED, "Archived"),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=30, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=STATUS_UNREAD, db_index=True
    )
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.subject
