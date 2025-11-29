# Standard Libraries
from abc import ABC
from typing import Generic, Optional, Type

# Own Libraries
from src.audit_hub.shared.generic_typing import EntityT, ModelT


class RepositoryI(ABC, Generic[ModelT, EntityT]):
    """Base interface for repository classes handling model and entity types.

    This class provides methods to access the registered model and entity
    classes for a repository.
    """

    def __init__(
        self,
        model_cls: Optional[Type[ModelT]] = None,
        entity_cls: Optional[Type[EntityT]] = None,
    ):
        """Initializes the repository with optional model and entity classes.

        Args:
            model_cls (Optional[Type[ModelT]]): The model class to register.
            entity_cls (Optional[Type[EntityT]]): The entity class to register.
        """

        self._cls_name = self.__class__.__name__
        self._model_cls = model_cls
        self._entity_cls = entity_cls

    def get_model_cls(self) -> Type[ModelT]:
        """Returns the registered model class for the repository.
        Raises:
            TypeError: If the model class is not registered.
        Returns:
            Type[ModelT]: The registered model class.
        """
        if not self._model_cls:
            raise TypeError(f"Model is not registered in {self._cls_name}")
        return self._model_cls

    def get_entity_cls(self) -> Type[EntityT]:
        """Returns the registered entity class for the repository.
        Raises:
            TypeError: If the entity class is not registered.
        Returns:
            Type[EntityT]: The registered entity class.
        """
        if not self._entity_cls:
            raise TypeError(f"Entity is not registered in {self._cls_name}")
        return self._entity_cls
