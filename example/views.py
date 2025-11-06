from django.http import HttpRequest
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.exceptions import APIException

from base_app.views import BaseViewSet

from .injector_provider import injector
from .serializers import (
    ArticleListRequestSerializer,
    ArticleSerializer,
)
from .policies import ArticleAccessPolicy
from .services import AbstractArticleService
from .models import Article

# Create your views here.
class ArticleViewSet(BaseViewSet):
    permission_classes = (ArticleAccessPolicy,)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service: AbstractArticleService = injector.get(AbstractArticleService)

    def get_queryset(self):
        return Article.objects.select_related('owner')

    def list(self, request: HttpRequest):
        serializer = ArticleListRequestSerializer(data=request.GET)
        serializer.is_valid(raise_exception=True)
        args = {**serializer.data, 'user': request.user}
        articles = self.service.get_list(**args)
        return Response(ArticleSerializer(articles, many=True).data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        article = self.service.create(serializer.data, request.user)
        return Response(ArticleSerializer(article).data, status=status.HTTP_201_CREATED)

    def retrieve(self, request: HttpRequest, pk=None):
        try:
            return Response(ArticleSerializer(self.service.get_by_id(pk)).data)
        except Exception as e:
            raise APIException(f"error {str(e)}")

    def update(self, request, pk=None):
        serializer = ArticleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        article = self.service.update(pk, serializer.data)
        return Response(ArticleSerializer(article).data, status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        article = self.service.get_by_id(pk)
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        args = {**model_to_dict(article), **request.data}
        del args['owner']
        result = self.service.update(pk, args)
        return Response(ArticleSerializer(result).data)
        pass

    def destroy(self, request, pk=None):
        self.service.delete(pk)
        return Response({"message": "Article deleted successfully"}, status=status.HTTP_200_OK)