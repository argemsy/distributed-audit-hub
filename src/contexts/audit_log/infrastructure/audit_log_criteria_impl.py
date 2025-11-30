# Standard Libraries
from dataclasses import dataclass, field

# Third-party Libraries
from django.db.models import Q

# Own Libraries
from src.shared.criteria import DjangoCriteriaSingle


@dataclass()
class AuditLogCriteriaSingle(DjangoCriteriaSingle[Q]):
    """
    Criteria class for filtering audit log queries using Django Q objects.

    This class allows combining custom filters with a default filter for
    non-deleted entries.
    """

    filters: Q = field(default_factory=Q)

    def get_filters(self) -> Q:
        q = self.filters
        q |= Q(is_deleted=False)
        return q
