from example.models import Article
from . import AbstractArticleRepository

from ..types import Article as ArticleType

class ArticleRepository(AbstractArticleRepository):
    def get_owner_list(self, user_id):
        queryset = Article.objects.filter(owner__id=user_id)
        return queryset
    
    def get_list(self):
        return Article.objects.all()

    def create(self, data: ArticleType) -> Article:
        return Article.objects.create(**data)

    def delete(self, id: str):
        return self.get_by_id(id).delete()