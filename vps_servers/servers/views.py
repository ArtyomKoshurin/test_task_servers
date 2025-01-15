from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
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

    @action(methods=['PUT', 'PATCH'], detail=False,
            url_path=r'(?P<pk>\d+)/update_status')
    def update_status(self, request, **kwargs):
        """Метод, позволяющий сменить статус виртуального сервера."""
        vps = get_object_or_404(VPS, id=kwargs['pk'])

        serializer = VPSStatusUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        vps.status = serializer.data["status"]
        vps.save(update_fields=["status"])

        return Response(f'Статус сервера {vps.uid} изменен на {vps.status}',
                        status=status.HTTP_200_OK)
