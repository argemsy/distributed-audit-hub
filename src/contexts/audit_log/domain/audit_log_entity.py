# Standard Libraries
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Optional


@dataclass(frozen=True, order=True)
class EntityAuditLog:
    """Represents an audit log entity with relevant metadata.

    This class stores information about an audit log entry,
    including object and creator details.
    """

    id: Optional[int] = field(default=None)
    object_id: Optional[str] = field(default=None)
    object_type: Optional[str] = field(default=None)
    created_by_id: Optional[int] = field(default=None)
    created_at: Optional[datetime] = field(
        default_factory=lambda: datetime.now(timezone.utc),
    )

    @classmethod
    def from_model(cls, instance: Any) -> "EntityAuditLog":
        """Creates an EntityAuditLog instance from a model instance.
        Args:
            instance (Any): The model instance to convert.
        Returns:
            EntityAuditLog: The created audit log entity.
        """
        return cls(
            id=instance.id,
            object_id=instance.object_id,
            object_type=instance.object_type,
            created_by_id=instance.created_by_id,
            created_at=instance.created_at,
        )

    def to_save(self) -> dict[str, Any]:
        """Returns a dictionary of the entity's data suitable for saving.

        The returned dictionary excludes the 'id' field.

        Returns:
            dict[str, Any]: The data to be saved.
        """
        kwargs = asdict(self)
        kwargs.pop("id", None)
        return kwargs

    # @property
    # def object_type_enum(self):
    #     pass
