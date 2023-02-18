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
from Payments.models import Favorite
from Reviews.serializers import LikeSerializer, Like
from Payments.serializers import FavoriteSerializer
# from rest_framework.response import Response


class PermissionMixin():
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]


class PacketViewSet(PermissionMixin, ModelViewSet):
    queryset = Packet.objects.all()
    serializer_class = PacketSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'price']

    @action(methods=['POST'], detail=True)   # detail=True - какое количнество элементов, тру - все
    def like(self, request, pk=None):
        packet = self.get_object()
        author = request.user # создадим автора из реквеста чтобы поле было автоматически заполнено
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # print(serializer.validated_data)
            try:
                like = Like.objects.get(packet=packet, author=author) # чтобы автора отслежаваить
                like.delete()
                # like.is_liked = not like.is_liked
                # like.save()
                message = 'disliked' # выводи сообщение о лайке или дизлайке
            except Like.DoesNotExist:
                Like.objects.create(packet=packet, is_liked=True, author=author) # если лайка нет, то создадим его
                message = 'liked'
            return Response(message, status=200)

    @action(methods=['POST'], detail=True)# detail=True -одлин объект
    def favorite(self, request, pk=None):
        packet = self.get_object()
        author = request.user
        serializer = FavoriteSerializer(data=request.data) # сериализуем наши данные (из джейсона в  питон файл)
        if serializer.is_valid(raise_exception=True):
            try:
                favorite = Favorite.objects.get(packet=packet, author=author)
                favorite.delete()
            except Favorite.DoesNotExist:
                Favorite.objects.create(packet=packet, author=author, is_favorite=True)
                message = 'deleted from favotites'
            return Response(message, status=200)


class PacketImageViewSet(PermissionMixin, ModelViewSet):
    queryset = PacketImage.objects.all()
    serializer_class = PacketImageSerializer
    

class CategoryViewSet(PermissionMixin, ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title']


class HotelViewSet(PermissionMixin, ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['title', 'country']
