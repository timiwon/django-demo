from injector import Module, provider, Injector, inject, singleton

from .repositories import (
    AbstractArticleRepository,
    ArticleRepository
)
from .services import (
    AbstractArticleService,
    ArticleService
)

class RepositoriesModule(Module):
    @singleton
    @provider
    def provide_article_repository(self) -> AbstractArticleRepository:
        return ArticleRepository()

class ServicesModule(Module):
    @singleton
    @provider
    def provide_article_service(self, repo: AbstractArticleRepository) -> AbstractArticleService:
        return ArticleService(repo=repo)

injector = Injector([ServicesModule(), RepositoriesModule()])
