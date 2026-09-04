from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


MAX_IMAGE_UPLOAD_SIZE = 5 * 1024 * 1024
ALLOWED_IMAGE_EXTENSIONS = ("jpg", "jpeg", "png", "webp")


validate_image_extension = FileExtensionValidator(
    allowed_extensions=ALLOWED_IMAGE_EXTENSIONS,
    message="Upload an image with a .jpg, .jpeg, .png, or .webp extension.",
)


def validate_image_file_size(uploaded_file):
    """Reject image uploads larger than five megabytes."""
    if uploaded_file.size > MAX_IMAGE_UPLOAD_SIZE:
        raise ValidationError(
            "Image files must be 5 MB or smaller.", code="file_too_large"
        )


image_upload_validators = [validate_image_extension, validate_image_file_size]
