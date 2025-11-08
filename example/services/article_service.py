from typing import Type
from injector import inject
from django.contrib.auth.models import AbstractUser
from django.db.models import Model

from . import AbstractArticleService
from ..repositories import AbstractArticleRepository
from ..types import Article, User

class ArticleService(AbstractArticleService):
    @inject
    def __init__(self, repo: AbstractArticleRepository):
        self.repo = repo

    def get_list(self, owner_only: bool, page: int, per_page: int, user: AbstractUser):
        if owner_only:
            return self.repo.get_owner_list(user.id)
        
        return self.repo.get_list()

    def create(self, data: Article, user: User):
        args = {**data, 'owner': user}
        return self.repo.create(args)
    
    def update(self, obj: Type[Model], data: Article):
        for field, value in data.items():
            setattr(obj, field, value)
        obj.save()

        return obj

    def delete(self, obj: Type[Model]):
        return obj.delete()