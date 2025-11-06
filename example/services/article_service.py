from injector import inject
from django.contrib.auth.models import AbstractUser

from . import AbstractArticleService
from ..repositories import AbstractArticleRepository
from ..types import Article, User

class ArticleService(AbstractArticleService):
    @inject
    def __init__(self, repo: AbstractArticleRepository):
        self.repo = repo

    def get_by_id(self, id: str):
        return self.repo.get_by_id(id)

    def get_list(self, owner_only: bool, page: int, per_page: int, user: AbstractUser):
        if owner_only:
            return self.repo.get_owner_list(user.id)
        
        return self.repo.get_list()

    def create(self, data: Article, user: User):
        args = {**data, 'owner': user}
        return self.repo.create(args)
    
    def update(self, id, data):
        print('--------')
        print(data)
        self.repo.update(id, data)
        return self.get_by_id(id)
    
    def delete(self, id):
        return self.repo.delete(id)