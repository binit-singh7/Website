import json
import logging
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

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


def _send_resend_email(to_email, subject, body, notification_type):
    payload = {
        "from": settings.DEFAULT_FROM_EMAIL,
        "to": [to_email],
        "subject": subject,
        "text": body,
        "reply_to": [settings.EMAIL_REPLY_TO],
    }
    request = Request(
        settings.RESEND_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {settings.RESEND_API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urlopen(request, timeout=settings.EMAIL_API_TIMEOUT) as response:
            if response.status not in {200, 201}:
                logger.error(
                    "Membership email provider returned an unexpected status",
                    extra={
                        "notification_type": notification_type,
                        "provider_status": response.status,
                    },
                )
                return False
    except HTTPError as error:
        logger.error(
            "Membership email provider rejected the request",
            extra={
                "notification_type": notification_type,
                "provider_status": error.code,
            },
        )
        return False
    except (TimeoutError, URLError, OSError):
        logger.error(
            "Membership email provider connection failed",
            extra={
                "notification_type": notification_type,
            },
        )
        return False
    except Exception:
        logger.exception(
            "Membership email provider failed unexpectedly",
            extra={"notification_type": notification_type},
        )
        return False

    return True


def send_membership_email(*, to_email, subject, body, notification_type):
    if settings.EMAIL_PROVIDER == "console":
        return send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL or None,
            [to_email],
            fail_silently=False,
        ) == 1

    if settings.EMAIL_PROVIDER == "resend":
        return _send_resend_email(to_email, subject, body, notification_type)

    logger.error(
        "Unsupported membership email provider",
        extra={"notification_type": notification_type},
    )
    return False


def _send_application_email(application, subject, body, notification_type):
    try:
        return send_membership_email(
            to_email=application.email,
            subject=subject,
            body=body,
            notification_type=notification_type,
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


def send_application_received_email(application):
    body = f"""Dear {application.full_name},

Thank you for applying to join Alliance Yuwa Club.

We have successfully received your membership application. Your application is currently pending review by the Alliance Yuwa Club team.

Application Reference: {application.pk}

We will contact you when the review is complete.

Regards,
Alliance Yuwa Club
Unity, Leadership, and Service
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
"""
    return _send_application_email(
        application,
        APPLICATION_REJECTED_SUBJECT,
        body,
        "application_rejected",
    )
