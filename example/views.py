from django.http import HttpRequest
from django.forms.models import model_to_dict
from rest_framework import status 
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from base_app.views import BaseViewSet, BasePagination

from .injector_provider import injector
from .serializers import (
    ArticleListRequestSerializer,
    ArticleSerializer,
)
from .policies import ArticleAccessPolicy
from .services import AbstractArticleService
from .models import Article

class LargeResultsSetPagination(BasePagination):
    page_size = 10

# Create your views here.
class ArticleViewSet(BaseViewSet):
    permission_classes = (ArticleAccessPolicy,)
    pagination_class = LargeResultsSetPagination # default page_size is 100

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.service: AbstractArticleService = injector.get(AbstractArticleService)

    def get_serializer_class(self):
        return ArticleSerializer

    def get_queryset(self):
        return Article.objects.select_related('owner')


    def list(self, request: HttpRequest):
        validated_data = self._validate_request_data(ArticleListRequestSerializer, request.GET)

        args = {**validated_data, 'user': request.user}
        articles = self.service.get_list(**args)

        return self._format_response(articles, many=True)

    def create(self, request):
        validated_data = self._validate_request_data(ArticleSerializer, request.data)
        article = self.service.create(validated_data, request.user)

        result = self.get_serializer(article)
        return Response(result.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request: HttpRequest, pk=None):
        try:
            return self._format_response(self.get_object())
        except Exception as e:
            raise APIException(f"error {str(e)}")

    def update(self, request, pk=None):
        validated_data = self._validate_request_data(ArticleSerializer, request.data)

        article = self.service.update(self.get_object(), validated_data)
        return self._format_response(article)

    def partial_update(self, request, pk=None):
        args = self._get_partial_update_data(ArticleSerializer, request.data)
        del args['owner']

        result = self.service.update(self.get_object(), args)
        return self._format_response(result)

    def destroy(self, request, pk=None):
        self.service.delete(self.get_object())
        return Response({"message": "Article deleted successfully"}, status=status.HTTP_200_OK)