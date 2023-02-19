# from django.contrib.auth.models import User
# from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny #IsAuthenticated,
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import PacketSerializer, PacketImageSerializer, CategorySerializer, HotelSerializer
from .models import Packet, PacketImage, Category, Hotel
from Reviews.models import Favorite
from Reviews.serializers import LikeSerializer, Like, FavoriteSerializer
# from Payments.serializers import FavoriteSerializer
# from rest_framework.response import Response


class PermissionMixin():
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class PacketViewSet(PermissionMixin, ModelViewSet):
    queryset = Packet.objects.get_queryset().order_by('id')
    serializer_class = PacketSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'price']

    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        packet = self.get_object()
        author = request.user 
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                like = Like.objects.get(packet=packet, author=author)
                like.delete()
                message = 'disliked' 
            except Like.DoesNotExist:
                Like.objects.create(packet=packet, is_liked=True, author=author)
                message = 'liked'
            return Response(message, status=200)

    @action(methods=['POST'], detail=True)
    def favorite(self, request, pk=None):
        packet = self.get_object()
        author = request.user
        serializer = FavoriteSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True):
            try:
                favorite = Favorite.objects.get(packet=packet, author=author)
                favorite.delete()
                message = 'deleted from favotites'
            except Favorite.DoesNotExist:
                Favorite.objects.create(packet=packet, author=author, is_favorite=True)
                message = 'added to favotites'
            return Response(message, status=200)


class PacketImageViewSet(PermissionMixin, ModelViewSet):
    queryset = PacketImage.objects.get_queryset().order_by('id')
    serializer_class = PacketImageSerializer
    

class CategoryViewSet(PermissionMixin, ModelViewSet):
    queryset = Category.objects.get_queryset().order_by('id')
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']


class HotelViewSet(PermissionMixin, ModelViewSet):
    queryset = Hotel.objects.get_queryset().order_by('id')
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'country']
