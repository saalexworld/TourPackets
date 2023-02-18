# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny #IsAuthenticated,

from .serializers import PacketSerializer, PacketImageSerializer, CategorySerializer, HotelSerializer
from .models import Packet, PacketImage, Category, Hotel
# from rest_framework.response import Response


class PermissionMixin():
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class PacketViewSet(PermissionMixin, ModelViewSet):
    """
    A ModelViewSet for listing or retrieving or updating or deleting packets.
    """
    queryset = Packet.objects.all()
    serializer_class = PacketSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['paket_title', 'price']


class PacketImageViewSet(PermissionMixin, ModelViewSet):
    """
    A ModelViewSet for listing or retrieving or updating or deleting images_packet.
    """
    queryset = PacketImage.objects.all()
    serializer_class = PacketImageSerializer
    

class CategoryViewSet(PermissionMixin, ModelViewSet):
    """
    A ModelViewSet for listing or retrieving or updating or deleting hotels.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']


class HotelViewSet(PermissionMixin, ModelViewSet):
    """
    A ModelViewSet for listing or retrieving or updating or deleting hotels.
    """
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'country']
