# Third-party Libraries
from django.db import models


class AuditMixin(models.Model):
    """Adds automatic created and updated timestamp fields to a model.

    This mixin provides `created_at` and `updated_at` fields that are
    automatically managed by Django.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        editable=False,
    )

    class Meta:
        abstract = True


class ActiveStateMixin(models.Model):
    """Adds active state and deactivation tracking fields to a model.

    This mixin provides fields to indicate if an object is active and to
    track deactivation details.
    """

    is_active = models.BooleanField(
        default=True,
        db_index=True,
    )
    deactivated_by_id = models.BigIntegerField(
        editable=False,
        db_index=True,
        blank=True,
        null=True,
    )
    deactivated_at = models.DateTimeField(
        blank=True,
        null=True,
        editable=False,
    )

    class Meta:
        abstract = True


class SoftDeleteMixin(models.Model):
    """Adds soft deletion fields to a model.

    This mixin provides fields to mark an object as deleted and to track
    deletion details.
    """

    is_deleted = models.BooleanField(
        default=False,
        db_index=True,
    )
    deleted_by_id = models.BigIntegerField(
        editable=False,
        db_index=True,
        blank=True,
        null=True,
    )
    deleted_at = models.DateTimeField(
        blank=True,
        null=True,
        editable=False,
    )

    class Meta:
        abstract = True
