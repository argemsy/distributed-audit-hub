# Standard Libraries
from abc import ABC, abstractmethod
from typing import Generic, Iterable, Optional

# Own Libraries
from src.shared.criteria import CriteriaList, CriteriaSingle
from src.shared.generic_typing import (
    EntityT,
    FilterT,
    ModelT,
    OrderByT,
)
from src.shared.repository_base import RepositoryI


class AuditLogRepository(RepositoryI[ModelT, EntityT], ABC):
    """Abstract base repository for audit log entities.

    This class defines the interface for saving and retrieving audit log
    entities in the repository.
    """

    @abstractmethod
    def save_instance(
        self, entity: Generic[EntityT], instance: Optional[ModelT] = None
    ) -> EntityT:
        pass

    @abstractmethod
    def get_instance(
        self, criteria: CriteriaSingle[FilterT]
    ) -> Optional[EntityT]:
        pass

    @abstractmethod
    def get_instances(
        self, criteria: CriteriaList[FilterT, OrderByT]
    ) -> Iterable[EntityT]:
        pass
