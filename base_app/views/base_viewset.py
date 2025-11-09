from abc import abstractmethod
from typing import Type
from django.shortcuts import get_object_or_404
from django.forms.models import model_to_dict
from rest_framework import viewsets, pagination
from rest_framework.response import Response
from rest_framework.serializers import Serializer

class BasePagination(pagination.PageNumberPagination):
    page_size = 100

    def get_paginated_response(self, data):
        return Response({
            'meta': {
                'links': {
                    'next': self.get_next_link(),
                    'previous': self.get_previous_link()
                },
                'total': self.page.paginator.count,
            },
            'results': data
        })

class BaseViewSet(viewsets.ViewSet, viewsets.GenericViewSet):
    pagination_class = BasePagination

    @abstractmethod
    def get_queryset(self):
        raise Exception('get_queryset method is required in extended class of BaseViewSet')
    
    @abstractmethod
    def get_serializer_class(self):
        raise Exception('get_serializer_class method is required in extended class of BaseViewSet')
    
    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def _validate_request_data(self, serializer_class: Type[Serializer], data):
        serializer: Type[Serializer] = serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        return serializer.data
    
    def _get_partial_update_data(self, serializer_class: Type[Serializer], data):
        obj = self.get_object()
        serializer = serializer_class(obj, data=data, partial=True)
        serializer.is_valid(raise_exception=True)

        args = {**model_to_dict(obj), **data}
        return args

    def _format_response(self, data, many=False):
        if many:
            page = self.paginate_queryset(data)
            if page is not None:
                serializer = self.get_serializer(page, many=many)
                return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(data, many=many)
        return Response({'result': serializer.data})
