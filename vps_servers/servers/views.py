from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404

from .models import VPS
from .serializers import VPSCreationSerializer, VPSInfoSerializer, VPSStatusUpdateSerializer


class VPSViewSet(viewsets.ModelViewSet):
    """Вьюсет для создания и просмотра виртуальных серверов."""
    queryset = VPS.objects.all()
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('uid', )

    def get_serializer_class(self):
        if self.request.method == "POST":
            return VPSCreationSerializer
        return VPSInfoSerializer
