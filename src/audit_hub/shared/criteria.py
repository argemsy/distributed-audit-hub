# Standard Libraries
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Generic, Optional

# Own Libraries
from src.audit_hub.shared.generic_typing import FilterT, OrderByT


@dataclass()
class CriteriaSingle(ABC, Generic[FilterT]):
    filters: Optional[FilterT] = field(default=None)

    @abstractmethod
    def get_filters(self) -> FilterT:
        pass


@dataclass()
class CriteriaList(CriteriaSingle[FilterT], Generic[FilterT, OrderByT], ABC):
    page: int = field(default=1)
    first: int = field(default=10)
    order_by: Optional[OrderByT] = field(default=None)


@dataclass()
class DjangoCriteriaSingle(CriteriaSingle[FilterT], ABC):
    pass


@dataclass()
class DjangoCriteriaList(CriteriaList[FilterT, OrderByT], ABC):
    pass
