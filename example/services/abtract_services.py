from abc import ABC, abstractmethod
from typing import Type
from django.contrib.auth.models import AbstractUser
from django.db.models import Model

from ..types import Article

class AbstractArticleService(ABC):
    @abstractmethod
    def get_list(self, owner_only: bool, user: AbstractUser): ...

    @abstractmethod
    def create(self, data: Article): ...

    @abstractmethod
    def update(self, obj: Type[Model], data: Article): ...

    @abstractmethod
    def delete(self, id: str): ...
