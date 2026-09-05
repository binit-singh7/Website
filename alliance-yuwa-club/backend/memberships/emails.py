import logging

from django.conf import settings
from django.core.mail import send_mail

logger = logging.getLogger(__name__)

APPLICATION_RECEIVED_SUBJECT = (
    "Alliance Yuwa Club Membership Application Received"
)
APPLICATION_APPROVED_SUBJECT = (
    "Your Alliance Yuwa Club Membership Application Has Been Approved"
)
APPLICATION_REJECTED_SUBJECT = (
    "Update on Your Alliance Yuwa Club Membership Application"
)


def _send_application_email(application, subject, body, notification_type):
    try:
        sent_count = send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [application.email],
            fail_silently=False,
        )
    except Exception:
        logger.exception(
            "Membership application email delivery failed",
            extra={
                "application_id": application.pk,
                "notification_type": notification_type,
            },
        )
        return False

    if sent_count != 1:
        logger.error(
            "Membership application email was not accepted by the backend",
            extra={
                "application_id": application.pk,
                "notification_type": notification_type,
            },
        )
        return False

    return True


def send_application_received_email(application):
    body = f"""Dear {application.full_name},

Thank you for applying to join Alliance Yuwa Club.

We have successfully received your membership application. Your application is currently pending review by the Alliance Yuwa Club team.

Application Reference: {application.pk}

We will contact you when the review is complete.

Regards,
Alliance Yuwa Club
Unity, Leadership, and Service
allianceyuwaclub@gmail.com
"""
    return _send_application_email(
        application,
        APPLICATION_RECEIVED_SUBJECT,
        body,
        "application_received",
    )


def send_application_approved_email(application):
    body = f"""Dear {application.full_name},

We are pleased to inform you that your membership application to Alliance Yuwa Club has been approved.

Welcome to Alliance Yuwa Club.

Our team will provide you with the next membership steps where applicable.

Regards,
Alliance Yuwa Club
Unity, Leadership, and Service
allianceyuwaclub@gmail.com
"""
    return _send_application_email(
        application,
        APPLICATION_APPROVED_SUBJECT,
        body,
        "application_approved",
    )


def send_application_rejected_email(application):
    body = f"""Dear {application.full_name},

Thank you for your interest in joining Alliance Yuwa Club.

After reviewing your membership application, we are unable to approve the application at this time.

We appreciate your interest and wish you the best.

Regards,
Alliance Yuwa Club
Unity, Leadership, and Service
allianceyuwaclub@gmail.com
"""
    return _send_application_email(
        application,
        APPLICATION_REJECTED_SUBJECT,
        body,
        "application_rejected",
    )
