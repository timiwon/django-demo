from abc import abstractmethod
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

class BaseViewSet(viewsets.ViewSet):
    @abstractmethod
    def get_queryset(self):
        raise Exception('get_queryset method required')

    def get_object(self):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj
