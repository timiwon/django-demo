from abc import ABC, abstractmethod
from django.contrib.auth.models import AbstractUser

from ..types import Article

class AbstractArticleService(ABC):
    @abstractmethod
    def get_by_id(self, id: str): ...

    @abstractmethod
    def get_list(self, owner_only: bool, user: AbstractUser): ...

    @abstractmethod
    def create(self, data: Article): ...

    @abstractmethod
    def update(self, id: str, data: Article): ...

    @abstractmethod
    def delete(self, id: str): ...
