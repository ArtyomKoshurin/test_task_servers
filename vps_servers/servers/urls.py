from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import VPSViewSet

app_name = 'servers'

router_vps = DefaultRouter()

router_vps.register('servers', VPSViewSet, basename='servers')

urlpatterns = [
    path('', include(router_vps.urls)),
]
