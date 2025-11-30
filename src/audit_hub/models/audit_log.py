# Third-party Libraries
from django.db import models

# Own Libraries
from src.shared.models import AuditMixin


class AuditLog(AuditMixin):
    object_id = models.CharField(max_length=50, db_index=True)
    object_type = models.CharField(max_length=100)
    created_by_id = models.BigIntegerField(
        blank=True,
        null=True,
        db_index=True,
    )

    class Meta:
        ordering = ["-created_at"]
