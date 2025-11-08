from abc import ABC, abstractmethod

from ..types import Article

class AbstractArticleRepository(ABC):
    @abstractmethod
    def get_owner_list(self, user_id: str): ...

    @abstractmethod
    def get_list(self): ...

    @abstractmethod
    def create(self, data: Article): ...

    @abstractmethod
    def delete(self, id: str): ...