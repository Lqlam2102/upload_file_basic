from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from rest_framework.viewsets import ViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.conf import settings

from app_media.models import Media
from app_media.serializers import MediaSerializers


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 1000

    def paginate_queryset(self, queryset, request, view=None):
        if 'all' in request.query_params:
            self.page_size = len(queryset)
            return super().paginate_queryset(queryset, request, view)
        return super().paginate_queryset(queryset, request, view)

    # custom thêm để hiện thêm total_pages với current_page_number
    def get_paginated_response(self, data):
        return Response({
            'page_size': len(data),
            'total_objects': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'current_page_number': self.page.number,
            'next': f'{settings.BASE_URL}{self.get_next_link()[21:]}' if self.get_next_link() else None,
            'previous': f'{settings.BASE_URL}{self.get_previous_link()[21:]}' if self.get_previous_link() else None,
            'results': data,
        })


class MediaAPIView(ViewSet, generics.ListAPIView, generics.DestroyAPIView, generics.UpdateAPIView,
                   generics.CreateAPIView, generics.RetrieveAPIView):
    def get_serializer_class(self):
        return MediaSerializers

    pagination_class = CustomPagination

    def get_permissions(self):
        return [permissions.AllowAny()]

    def get_queryset(self):
        list_obj = Media.objects.filter(is_active=True)
        return list_obj
