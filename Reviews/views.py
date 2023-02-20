from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Like, Rating, Comment, LikeComment, Favorite
from .serializers import CommentSerializer, RatingSerializer, \
LikeCommentSerializer, LikeSerializer, FavoriteSerializer
from .permissions import IsAuthorOrReadOnly


class PermissionMixin:
    def get_permissions(self):
        if self.action == 'create':
            permissions = [IsAuthenticated]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthorOrReadOnly]
        else:
            permissions = [AllowAny]
        return [permission() for permission in permissions]


class LikeCommentViewSet(PermissionMixin,ModelViewSet):
    queryset = LikeComment.objects.get_queryset().order_by('id')
    serializer_class = LikeCommentSerializer


class CommentViewSet(PermissionMixin,ModelViewSet):
    queryset = Comment.objects.get_queryset().order_by('id')
    serializer_class = CommentSerializer

    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        comment = self.get_object()
        author = request.user
        serializer = LikeCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                like = LikeComment.objects.get(comment=comment, author=author)
                like.delete()
                message = 'disliked'
            except LikeComment.DoesNotExist:
                LikeComment.objects.create(comment=comment, is_liked=True, author=author)
                message = 'liked'
            return Response(message, status=200)


class RatingViewSet(PermissionMixin,ModelViewSet):
    queryset = Rating.objects.get_queryset().order_by('id')
    serializer_class = RatingSerializer


class LikeViewSet(PermissionMixin,ModelViewSet):
    queryset = Like.objects.get_queryset().order_by('id')
    serializer_class = LikeSerializer


class FavoriteViewSet(PermissionMixin, ModelViewSet):
    queryset = Favorite.objects.get_queryset().order_by('id')
    serializer_class = FavoriteSerializer
