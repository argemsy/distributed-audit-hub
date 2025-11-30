# Standard Libraries
from typing import Any, Optional

# Third-party Libraries
from django.db.models import Q

# Own Libraries
from src.audit_hub.models import AuditLogModel
from src.contexts.audit_log.domain.audit_log_entity import (
    EntityAuditLog,
)
from src.contexts.audit_log.domain.audit_log_repository import (
    AuditLogRepository,
)
from src.shared.criteria import (
    DjangoCriteriaList,
    DjangoCriteriaSingle,
)
from src.shared.generic_typing import OrderByT


class AuditLogDjangoRepositoryImpl(
    AuditLogRepository[
        AuditLogModel,
        EntityAuditLog,
    ]
):
    """Django implementation of the audit log repository.

    This class provides methods to save and retrieve audit log entities using
    Django ORM.
    """

    def __init__(self):
        """
        Initializes the repository with the AuditLogModel and EntityAuditLog
        classes.
        """
        super().__init__(model_cls=AuditLogModel, entity_cls=EntityAuditLog)

    def get_instance(
        self, criteria: DjangoCriteriaSingle[Q]
    ) -> Optional[EntityAuditLog]:
        """Retrieves a single audit log entity matching the given criteria.

        Args:
            criteria (DjangoCriteriaSingle[FilterT, OrderByT]): The criteria
            to filter audit log entries.

        Returns:
            Optional[EntityAuditLog]: The matching audit log entity, or None
                if not found.
        """

        model_cls = self.get_model_cls()
        qs = model_cls.objects.filter(criteria.get_filters())
        if not (instance := qs.first()):
            return None
        entity_cls = self.get_entity_cls()

        return entity_cls.from_model(instance=instance)

    def get_instances(
        self, criteria: DjangoCriteriaList[Q, OrderByT]
    ) -> list[EntityAuditLog]:
        """Retrieves a list of audit log entities matching the given criteria.

        Args:
            criteria (DjangoCriteriaList[FilterT, OrderByT]): The criteria to
                filter audit log entries.

        Returns:
            list[EntityAuditLog]: A list of matching audit log entities.
        """
        model_cls = self.get_model_cls()
        qs = model_cls.objects.filter(criteria.get_filters())
        entity_cls = self.get_entity_cls()

        return [entity_cls.from_model(instance=instance) for instance in qs]

    def save_instance(
        self,
        entity: EntityAuditLog,
        instance: Optional[AuditLogModel] = None,
    ) -> EntityAuditLog:
        """Saves an audit log entity to the database.

        Args:
            entity (EntityAuditLog): The audit log entity to save.
            instance (Optional[AuditLogModel]): An optional existing model
            instance to update.

        Returns:
            EntityAuditLog: The saved audit log entity.
        """
        data_to_save: dict[str, Any] = entity.to_save()

        model_cls = self.get_model_cls()
        instance = model_cls(**data_to_save)
        instance.save()

        entity_cls = self.get_entity_cls()
        return entity_cls.from_model(instance=instance)
